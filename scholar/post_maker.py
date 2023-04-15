import re
from pathlib import Path
from scholar.database import Paper
from scholar.api import ARXIV_GROUP_MAP 

POST_DIR = Path("_posts/")


def sanitize_filename(filename: str) -> str:
    """Sanitize a filename to make it safe for use on Windows and Linux."""

    # Replace all symbols with spaces
    sanitized = re.sub(r"[^a-zA-Z0-9\s]", " ", filename)
    sanitized = sanitized.strip()
    sanitized = sanitized.replace(" ", "-")
    sanitized = sanitized.replace("--", "-")

    if not sanitized:
        sanitized = "default_filename"

    return sanitized.lower()[:64]


def make_md_post(paper: Paper) -> None:
    """Make a post for the given paper."""

    # Create file name
    pub_date = paper.published_on.strftime("%Y-%m-%d")
    clean_title = sanitize_filename(paper.title)
    file_name = f"{pub_date}-{clean_title}.md"

    if paper.arxiv_group_tag:
        category = ARXIV_GROUP_MAP[paper.arxiv_group_tag]
    else:
        category = "Uncategorized"

    # Create file content
    content = f"""---
    title: "{paper.title}"
    categories:
      - {category}
    tags:
      - auto
    ---
    {paper.publication_info_summary}

    {paper.snippet}

    Link to paper: [{paper.link}]({paper.link})
    """.replace(
        "    ", ""
    )

    # Write file
    with open(POST_DIR / file_name, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Markdown file created successfully: {paper.title}")


def make_all() -> None:
    papers = Paper.select()
    for paper in papers:
        make_md_post(paper)


if __name__ == "__main__":
    make_all()
