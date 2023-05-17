---
layout: page
title: Simulation-based inference
permalink: /
---

## Introduction

Simulators are the modern manifestation of scientific theories. They implement mechanistic models of the underlying natural phenomena of interest as well as models for the instruments used to observe those phenomena. The expressiveness of programming languages facilitates the development of complex, high-fidelity simulations and the power of modern computing provides the ability to generate synthetic data from them. The flexibility of simulators has made them critical research tools (and major cyberinfrastructure investments) for predicting how systems will behave across many areas of science and engineering. Unfortunately, despite their predictive power, these *simulators are poorly suited for statistical inference*, which is a core aspect of data-intensive science. To meet this challenge, there are an emerging set of techniques for simulation-based inference (SBI).

Simulation-based inference is the next step in the methodological evolution of statistical practice in the sciences. SBI provides qualitatively new capabilities that can transform scientific practice in fields as diverse as evolutionary biology, systems biology, neuroscience, gravitational wave astronomy, dark matter astrophysics, cosmology, and particle physics. Inference problems in these areas are challenging because they involve high-dimensional, richly-structured spaces. Empowering domain scientists with the ability to directly infer from data the properties of the underlying mechanistic models that they are developing would be transformative.

SBI has also proven to be an effective lingua franca that facilitates communication between domain scientists and methodological experts, supports convergence research, and accelerates cross-pollination of ideas between fields. 

## Selected Resources

### Papers

The plan is to turn this page into a crowd-sourced community resource that can collect recent papers including methodological developments and applications. Here are some links to get started:

**Reviews**
 * [The frontier of simulation-based inference](https://doi.org/10.1073/pnas.1912789117) review by Kyle Cranmer, Johann Brehmer, and Gilles Louppe

 * Google Scholar searches for ["Simulation-based inference"](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C33&q=%22simulation-based+inference%22+&btnG=),  ["likelihood-free"](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C33&q=%22likelihood-free%22+&btnG=), and ["Approximate Bayesian Computation"](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C33&as_vis=1&q=%22approximate+bayesian+computation%22&btnG=)


**Applications**

* **Particle Physics**: [Simulation-based inference methods for particle physics](https://arxiv.org/abs/2010.06439) by Johann Brehmer and Kyle Cranmer in "Artificial Intelligence for Particle Physics", World Scientific Publishing Co.

* **Computational Neuroscience**: [Training deep neural density estimators to identify mechanistic models of neural dynamics](https://elifesciences.org/articles/56261) by Pedro J Gonçalves, Jan-Matthis Lueckmann, Michael Deistler, Marcel Nonnenmacher, Kaan Öcal, Giacomo Bassetto, Chaitanya Chintaluri, William F Podlaski, Sara A Haddad, Tim P Vogels, David S Greenberg, Jakob H Macke

* **Gravitational Wave Astronomy**: [Real-Time Gravitational Wave Science with Neural Posterior Estimation](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.241103) by Maximilian Dax, Stephen R. Green, Jonathan Gair, Jakob H. Macke, Alessandra Buonanno, and Bernhard Schölkopf

* **Gravitational Wave Astronomy**: [Peregrine: Sequential simulation-based inference for gravitational wave signals](https://arxiv.org/abs/2304.02035) by Uddipta Bhardwaj, James Alvey, Benjamin Kurt Miller, Samaya Nissanke, Christoph Weniger

* **Astroparticle Physics**: [Inferring dark matter substructure with astrometric lensing beyond the power spectrum](https://iopscience.iop.org/article/10.1088/2632-2153/ac494a/meta) by Siddharth Mishra-Sharma

* **Astroparticle Physics**: [A neural simulation-based inference approach for characterizing the Galactic Center](https://arxiv.org/abs/2110.06931) by Siddharth Mishra-Sharma, Kyle Cranmer

* **Climate Science**: [Model calibration using ESEm v1.1.0 – an open, scalable Earth system emulator](https://gmd.copernicus.org/articles/14/7659/2021/gmd-14-7659-2021.html) by Duncan Watson-Parris, Andrew Williams, Lucia Deaconu, and Philip Stier

* **Cosmology**: [Simulation-Based Inference of Strong Gravitational Lensing Parameters](https://arxiv.org/abs/2112.05278) by Ronan Legin, Yashar Hezaveh, Laurence Perreault Levasseur, Benjamin Wandelt

* **Cosmology**: [Simulation-Based Inference of Reionization Parameters From 3D Tomographic 21 cm Lightcone Images](https://arxiv.org/abs/2105.03344) by Zhao, Xiaosheng ;  Mao, Yi ;  Cheng, Cheng ;  Wandelt, Benjamin D.

* **Genomics**: [Addressing uncertainty in genome-scale metabolic model reconstruction and analysis](https://link.springer.com/article/10.1186/s13059-021-02289-z) by David B. Bernstein, Snorre Sulheim, Eivind Almaas & Daniel Segrè in Genome Biology volume 22, Article number: 64 (2021)
> Furthermore, genome-scale metabolic models (GEMs) can be used to simulate disparate types of ‘omics data, even though the explicit calculation of likelihoods may be intractable. Thus, the use of “simulation-based” Bayesian inference approaches is a promising route for informing GEM structure and parameters from data [198]. However, scaling Bayesian approaches up to deal with the large space of possible GEM reconstructions is an open, exciting and challenging research direction.

* **Evolutionary Biology**: [Simulation-based inference of evolutionary parameters from adaptation dynamics using neural networks](https://www.biorxiv.org/content/10.1101/2021.09.30.462581v1.abstract) by  Grace Avecilla,  Julie N. Chuong, Fangfei Li,  Gavin Sherlock,  David Gresham,  Yoav Ram

* **Evolutionary Biology**: [Universal probabilistic programming offers a powerful approach to statistical phylogenetics]() by Fredrik Ronquist, Jan Kudlicka, Viktor Senderov, Johannes Borgström, Nicolas Lartillot, Daniel Lundén, Lawrence Murray, Thomas B. Schön & David Broman 

* **Global Health**: [Simulation-Based Inference for Global Health Decisions](https://arxiv.org/abs/2005.07062) by Christian Schroeder de Witt, Bradley Gram-Hansen, Nantas Nardelli, Andrew Gambardella, Rob Zinkov, Puneet Dokania, N. Siddharth, Ana Belen Espinosa-Gonzalez, Ara Darzi, Philip Torr, Atılım Güneş Baydin

* **Robotics**: [Simulation-based Bayesian inference for multi-fingered robotic grasping](https://arxiv.org/abs/2109.14275) by Norman Marlier, Olivier Brüls, Gilles Louppe

### Other curated resources list

- [Awesome neural SBI](https://github.com/smsharma/awesome-neural-sbi)