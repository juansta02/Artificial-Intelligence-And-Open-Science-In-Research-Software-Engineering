import os

def test_xml_files_exist():
    xml_folder = "data/xml"
    files = os.listdir(xml_folder)
    assert len(files) > 0