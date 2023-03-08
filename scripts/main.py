from bs4 import BeautifulSoup
from collections import defaultdict
import os
import json
from grobid_client.grobid_client import GrobidClient
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "./papers", "./papers/results",
               consolidate_citations=True, n=20, force=False, verbose=True)

directory = "./papers/results"
frecuenciesKeywords = defaultdict(int)
histogramFigures = []
linksPerPaper = defaultdict(list)

for file in os.scandir(directory):
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
    word_cloud.to_file(f'./papers/results/images/{filename}.png')

    # histogram of the frecuency of figures
    histogramFigures.append(len(soup.find_all('figure')))
    plt.hist(histogramFigures)
    plt.savefig('figures_histogram.png')

    # extract links
    for link in soup.find_all('ptr'):
        linksPerPaper[filename].append(link.get('target'))

with open("./papers/results/links/links.json", "w") as outfile:
    json.dump(linksPerPaper, outfile)
