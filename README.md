
# Apaper
Analysis of papers using the grobid tool [1] and python scripts.
The purpose of this repository is to perform a series of tasks using the tools learned in class. 
The task are:

> Follow the best practices taught in class to perform an analysis over
> 10 open-access articles using Grobid (or other text analysis tools).
> Your program should:
> - Draw a keyword cloud based on the abstract information
> - Create a visualization showing the number of figures per article.
> - Create a list of the links found in each paper.

From  ‘Open Science and Artificial Intelligence in Research Software Engineering: Introduction’ by Daniel Garijo and Oscar Corcho at http://www.oeg-upm.net.

# Prerequisites

 - Grobid 0.7.2+ for pdf analysis (see https://github.com/kermitt2/grobid/)
 - Poetry for virtual enviroment (see https://python-poetry.org/docs/managing-environments/)
 
# Usage
Clone the repository:

    git clone https://github.com/sbayonag/Apaper.git
    cd Apaper
Poetry virtualization:

    poetry install

Create a directory called papers and put there all the pdfs you want to analyse.
Run your grobid installation on the 8070 port (default port) I use this command:

    docker run --rm --gpus all -p 8070:8070 -p 8071:8071 grobid/grobid:0.7.2
omit '--gpus all' if you don't have an nvidia gpu or plan not to use it.

Run the script inside a poetry shell:

    poetry shell
    python3 scripts/main.py

# Results

 1. Visualization of keywords at ./papers/results/images with the paper
    title and png extension. It uses wordcloud (see https://amueller.github.io/word_cloud/index.html) 
 2. Histrogram of the number of figures per article at ./papers/results/images/figures_histogram.png using matplotlib (see https://matplotlib.org/) 
 3. List of links per paper in json format in ./papers/results/links with the paper title and json extension

# Referencias
1. GROBID (2008-2022) <https://github.com/kermitt2/grobid>
