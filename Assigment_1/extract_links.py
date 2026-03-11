import os
import re
from bs4 import BeautifulSoup

xml_folder = "data/xml"
url_pattern = r"https?://[^\s]+"

with open("results/links.txt", "w") as output:

    for file in os.listdir(xml_folder):

        if file.endswith(".xml"):

            with open(os.path.join(xml_folder, file), encoding="utf-8") as f:

                soup = BeautifulSoup(f, "xml")

                output.write(f"\n{file}\n")

                # Links en atributos target
                for r in soup.find_all("ref"):
                    link = r.get("target")
                    if link and link.startswith(("http://", "https://")):
                        output.write(link + "\n")

                # Links en texto
                text_links = re.findall(url_pattern, soup.get_text())

                for link in text_links:
                    output.write(link + "\n")