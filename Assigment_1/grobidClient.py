import requests
import os

pdf_folder = "data/pdf"
xml_folder = "data/xml"

url = "http://localhost:8070/api/processFulltextDocument"

for file in os.listdir(pdf_folder):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(pdf_folder, file)

        with open(pdf_path, "rb") as f:

            files = {"input": (file, f, "application/pdf")}
            response = requests.post(url, files=files)

        xml_name = file.replace(".pdf", ".xml")
        xml_path = os.path.join(xml_folder, xml_name)

        with open(xml_path, "w", encoding="utf-8") as out:
            out.write(response.text)

        print(f"Processed {file}")