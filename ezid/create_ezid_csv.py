import json
import csv

def format_authors(authors):
    return ", ".join(authors)

def write_csv(papers, ofile = "accepted_ezid.csv"):
    with open(ofile, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for p in papers:
            if 'archival_status' not in p or p['archival_status'] == "Archival":
                title = p['title'] #.encode('utf-8')
                authors = format_authors(p['authors']) #.encode('utf-8')
                url = "https://www.akbc.ws/2020/papers/" + p['forum_id']
                writer.writerow([title, authors, url])

def read_from_json(ifile = "accepted.json"):
    with open(ifile, 'r') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    papers = read_from_json()
    # print(papers)
    write_csv(papers)
