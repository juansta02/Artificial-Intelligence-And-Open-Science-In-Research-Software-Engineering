import os
from bs4 import BeautifulSoup

xml_folder = "data/xml"

output = open("results/links.txt","w")

for file in os.listdir(xml_folder):

    if file.endswith(".xml"):

        with open(os.path.join(xml_folder, file), encoding="utf-8") as f:

            soup = BeautifulSoup(f, "xml")

            output.write(f"\n{file}\n")

            refs = soup.find_all("ref")

            for r in refs:

                if r.get("target"):
                    output.write(r["target"] + "\n")