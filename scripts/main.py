from bs4 import BeautifulSoup
from collections import defaultdict
import os
import json
from grobid_client.grobid_client import GrobidClient
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

outputDirectory = "./papers/results"
client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "./papers", outputDirectory,
               consolidate_citations=True, n=20, force=False, verbose=True)

frecuenciesKeywords = defaultdict(int)
histogramFigures = []
linksPerPaper = defaultdict(list)

for file in os.scandir(outputDirectory):
    if file.is_dir():
        continue
    if not file.name.endswith(".xml"):
        print(f"Ignoring file that doesn't have '.xml' extension: {file.name}")
        continue

    filename = file.name[:-4]
    with open(file.path, 'r') as tei:
        soup = BeautifulSoup(tei, 'xml')

    # Wordcloud based on abstract.
    word_cloud = WordCloud(
        random_state=1,
        background_color="salmon",
        colormap="Pastel1",
        collocations=False,
        stopwords=STOPWORDS,
    ).generate(soup.find('abstract').get_text(strip=True))
    word_cloud.to_file(f'{outputDirectory}/images/{filename}.png')

    # histogram of the frecuency of figures
    histogramFigures.append(len(soup.find_all('figure')))
    plt.hist(histogramFigures)
    plt.savefig(f'{outputDirectory}/images/figures_histogram.png')

    # extract links
    for link in soup.find_all('ptr'):
        linksPerPaper[filename].append(link.get('target'))

with open("./papers/results/links/links.json", "w") as outfile:
    json.dump(linksPerPaper, outfile)
