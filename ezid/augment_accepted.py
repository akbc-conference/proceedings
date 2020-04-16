import json
import csv

def read_from_json(ifile = "accepted.json"):
    with open(ifile, 'r') as f:
        data = json.load(f)
    return data

def read_csv(ifile = "gen_dois.csv"):
    dois = []
    with open(ifile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dois.append(row[1])
    return dois

def augment_data(papers, dois):
    idx = 0
    for p in papers:
        if p['archival status'] == "Archival":
            p["doi"] = dois[idx]
            idx += 1
        else:
            p["doi"] = ""

def save_to_json(papers, ofile = "accepted_aug.json"):
    with open(ofile, 'w') as f:
        json.dump(papers, f, indent=2)

if __name__ == "__main__":
    papers = read_from_json()
    dois = read_csv()
    assert len([p for p in papers if p['archival status'] == "Archival"]) == len(dois)
    augment_data(papers, dois)
    save_to_json(papers)