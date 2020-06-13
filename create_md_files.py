import argparse
import json
from pprint import pprint

def parse_arguments():
  parser = argparse.ArgumentParser(description="Write Markdown pages for each paper")
  parser.add_argument("--output-md", default="../akbc-2020/pages/proceedings", help="Directory where generated markdown will be stored")
  parser.add_argument("--papers", default="papers.json", help="JSON file all the paper info")
  parser.add_argument("--output-pdf", default="../akbc-2020/assets/pdfs", help="Directory where files will be stored")
  return parser.parse_args()

def write_md(paper, dir):
  with open(dir + "/" + paper["forum_id"] + ".md", 'w') as f:
    f.write("""---
layout: paper-page
forum_id: {fid}
permalink: /papers/{fid}
header:
    image_fullwidth: "generic-gradient.png"
---
    """.format(fid=paper['forum_id'], title=paper['title']))

# def write_pdf(paper, dir):


if __name__ == "__main__":
  args = parse_arguments()
  papers = json.load(open(args.papers))

  for paper in papers:
    write_md(paper, args.output_md)
