# proceedings
code to create/manage proceedings

## Accepted Papers

This will create a `papers.json` with all the relevant information from OpenReview for all the accepted papers. This file is compatible with the AKBC website, i.e. you can put this directly in `_data` on the AKB website.

Downloaded by running `accepted_papers.py` after installing the following:

```
pip install openreview-py argparse wget
```

## Create MD Files 

We create a page for each paper on the AKBC website. This script does that, based on `papers.json`, along with downloading and storing the PDF files as well.