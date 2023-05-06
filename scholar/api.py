import os
import re
import json
import requests
import arxiv
import datetime
import difflib
from time import sleep
from typing import Optional
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")

# GROUP is arxiv top level category
ARXIV_GROUP_MAP = json.load(open("scholar/arxiv_group.json"))

# CATEGORY is arxiv sub category
ARXIV_CATEGORY_MAP = json.load(open("scholar/arxiv_category.json"))


def timeout(func, duration=0.5):
    """Delay the execution of a function."""

    def wrapper(*args, **kwargs):
        sleep(duration)
        return func(*args, **kwargs)
    return wrapper


def get_arxiv_category_map() -> dict:
    url = "https://arxiv.org/category_taxonomy"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find("div", id="category_taxonomy_list").select("h4")

    category_mapping = {}
    for record in data:
        text = str(record)
        category = re.search(r"<h4>(.*?) <span>", text).group(1)
        full_name = re.search(r"<span>\((.*?)\)</span>", text).group(1)
        category_mapping[category] = full_name

    return category_mapping


def get_bibtex(arxiv_id: str) -> Optional[str]:
    url = f"https://arxiv.org/bibtex/{arxiv_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch BibTeX for arXiv ID {arxiv_id}")
        return None


def to_category(arxiv_category: Optional[str]) -> str:
    """Convert arxiv category to group."""

    if arxiv_category is None:
        return None
    group_tag = arxiv_category.split(".")[0]
    return ARXIV_GROUP_MAP.get(group_tag, None)

def to_doi(biorxiv_link: str) -> str:
    """Convert biorxiv link to doi."""

    if biorxiv_link is None:
        return None
    doi = biorxiv_link.replace("https://www.biorxiv.org/content/", "")
    doi = doi.replace("v1", "").replace("v2", "").replace("v3", "")
    doi = doi.replace(".abstract", "").replace(".full", "").replace(".short", "")
    return doi


@timeout
def query_biorxiv(doi:str) -> dict:
    """Query biorxiv for a paper with the given doi."""

    url = f"https://api.biorxiv.org/details/biorxiv/{doi}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['collection'][0]
        return {
            "authors": data["authors"],
            "doi": data["doi"],
            "category": data["category"].capitalize(),
        }


@timeout
def query_arxiv(title: str, threshold: float = 0.8) -> arxiv.Result:
    """Query arxiv for a paper with the given title."""
    search = arxiv.Search(query=f"ti:{title.replace(':', ' ')}", max_results=1)

    # If no results, return
    try:
        result = next(search.results())
    except StopIteration:
        return

    # Double check that the title matches close enough
    r = difflib.SequenceMatcher(None, title, result.title).ratio()
    if r > threshold:
        return {
            "authors": ", ".join([str(author) for author in result.authors]),
            "doi": result.doi,
            "arxiv_category_tag": result.primary_category,
            "arxiv_id": result.entry_id.split("/")[-1],
            "category": to_category(result.primary_category),
        }


def format_serp_result(result: dict) -> dict:
    """Format the SERP API results."""

    _tmp = result["snippet"].split(" days ago - ")
    snippet = _tmp[1]
    days_since_added = int(_tmp[0])
    published_on = datetime.datetime.now() - datetime.timedelta(days=days_since_added)
    publication_info_summary = result["publication_info"]["summary"]

    try:
        citation_backlink = result["inline_links"]["cited_by"]["link"]
    except KeyError:
        citation_backlink = None

    return {
        "result_id": result["result_id"],
        "published_on": published_on,
        "title": result["title"],
        "days_since_added": days_since_added,
        "publication_info_summary": publication_info_summary,
        "journal": publication_info_summary.split(" - ")[2],
        "doi": to_doi(result["link"]),
        "link": result["link"],
        "snippet": snippet,
        "citation_backlink": citation_backlink,
    }


def query_serp(
    url: str = None, term: str = None, more_results: bool = False
) -> Optional[dict]:
    """Query the SERP API for snippets containing the given term.

    Args:
        url (str): API URL. If None, use the default.
        term (str): The term to search for.
        more_results (bool): If true search in everything instead of abstract.
    """
    params = {"api_key": SERP_API_KEY}
    scisbd = 2 if more_results else 1

    if url is None:
        url = "https://serpapi.com/search"
        params.update(
            {
                "engine": "google_scholar",
                "q": term,
                "hl": "en",
                "num": 20,  # Maxed out at 20
                "scisbd": scisbd,
                "as_vis": 1,
            }
        )

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        data["formatted_results"] = [
            format_serp_result(result) for result in data["organic_results"]
        ]
        return data
    else:
        print(
            f"Request failed with status code {response.status_code}: {response.text}"
        )
