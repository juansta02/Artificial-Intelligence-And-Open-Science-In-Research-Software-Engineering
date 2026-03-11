import os
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

xml_folder = "data/xml"

abstracts = []

for file in os.listdir(xml_folder):

    if file.endswith(".xml"):

        xml_path = os.path.join(xml_folder, file)

        with open(xml_path, encoding="utf-8") as f:

            soup = BeautifulSoup(f, features="xml")

            abstract = soup.find("abstract")

            if abstract:
                text = abstract.get_text()
                abstracts.append(text)

full_text = " ".join(abstracts)

wc = WordCloud(width=800, height=400, background_color="white").generate(full_text)
plt.imshow(wc)
plt.axis("off")
plt.savefig("results/wordcloud.png")