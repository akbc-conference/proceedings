import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def read_from_json(ifile = "accepted.json"):
    with open(ifile, 'r') as f:
        data = json.load(f)
    return data

def add_element(parent, name, text):
    tmp = ET.SubElement(parent, name)
    tmp.text = text

def create_XML(papers):
    root = ET.Element('dblpsubmission')
    proc = ET.SubElement(root, 'proceedings')
    # Header
    # key = ET.SubElement(proc, 'key')
    # key.text = "akbc" (unknown the first time)
    editors = ["Dipanjan Das", "Hannaneh Hajishirzi", "Andrew McCallum", "Sameer Singh"]
    for e in editors:
        ed = ET.SubElement(proc, 'editor')
        ed.text = e
    title = ET.SubElement(proc, 'title')
    title.text = "1st Conference on Automated Knowledge Base Construction (AKBC) 2020"
    year = ET.SubElement(proc, 'year')
    year.text = "2020"
    # Conference
    conf = ET.SubElement(proc, 'conf')
    add_element(conf, 'acronym', "AKBC")
    add_element(conf, 'number', "1")
    add_element(conf, 'location', "Virtual")
    add_element(conf, 'date', "June 22-24, 2020")
    add_element(conf, 'url', "https://www.akbc.ws/2020/")
    # TOC
    toc = ET.SubElement(proc, 'toc')
    for p in papers:
        if 'archival status' not in p or p['archival status'] == "Archival":
            publ = ET.SubElement(toc, 'publ')
            for a in p['authors']:
                add_element(publ, 'author', a)
            add_element(publ, 'title', p['title'])
            add_element(publ, 'doi', p['doi'].replace("doi:", ""))
            add_element(publ, 'ee', "https://www.akbc.ws/2020/papers/"+p['forum_id'])
    return root

if __name__ == "__main__":
    papers = read_from_json()
    data = create_XML(papers)
    with open("proceedings.xml", "w") as f:
        f.write("<!DOCTYPE dblpsubmission SYSTEM \"dblpsubmission.dtd\">\n")
        f.write("<?xml-stylesheet type=\"text/xsl\" href=\"dblpsubmission.xsl\" ?>\n")
        xmlstr = minidom.parseString(ET.tostring(data)).toprettyxml(indent="  ")
        f.write(xmlstr)
    
            