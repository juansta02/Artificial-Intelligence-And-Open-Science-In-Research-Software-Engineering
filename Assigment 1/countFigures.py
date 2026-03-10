import os
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

xml_folder = "data/xml"

papers = []
counts = []

for file in os.listdir(xml_folder):

    if file.endswith(".xml"):

        with open(os.path.join(xml_folder, file), encoding="utf-8") as f:

            soup = BeautifulSoup(f, "xml")

            figures = soup.find_all("figure")

            papers.append(file.replace(".xml",""))
            counts.append(len(figures))

plt.bar(papers, counts)

plt.ylabel("Number of figures")
plt.xlabel("Paper")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("results/figures_per_paper.png")