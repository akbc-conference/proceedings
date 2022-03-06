# Generate DOIs

## Copy list of papers

Copy over the `papers.json` created from `accepted_papers.py`. 

```
cp ../papers.json accepted.json
```

## Prepare Metadata

Make sure URLs for PDFs in `create_ezid_csv` is correct.

Run `create_ezid_csv` to generate the `accepted_ezid.csv` file, which is just a CSV version containing titles and authors.

```
python create_ezid_csv.py
```

1(b). _Optional_: Check to make sure `ezid_mappings_dc` looks okay.

## Generate DOIs

Generate DOIs for the papers (submits to EZID):

Note: Uses Python2, which you might have to call explicitly.

```
python2 batch-register.py -c <username>:<password> -s <shoulder> mint ezid_mappings_dc accepted_ezid.csv > gen_dois.csv
```

Authentication is for [EZID](https://ezid.cdlib.org/), which is where you see the shoulder (that looks like `doi:10.24432/C5`).

If you want to preview the metadata, use `-p`.
If you want to test, remove `-p` and use `doi:10.5072/FK2` as the shoulder.

## Augment JSON

Augment the JSON file with this additional data, might be useful.

Run `augment_accepted.py`, and copy over `accepted_aug.json` to `_data/accepted.json` of the website.

```
python augment_accepted.py
```