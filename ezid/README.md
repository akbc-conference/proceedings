# Generate DOIs

## Prepare Metadata

Run `create_ezid_csv` to generate the `accepted_ezid.csv` file, which is just a CSV version containing titles and authors.

1(b). _Optional_: Check to make sure `ezid_mappings_dc` looks okay.

## Generate DOIs

Generate DOIs for the papers (submits to EZID):

```
./batch-register.py -c <username>:<password> -s <shoulder> mint ezid_mappings_dc accepted_ezid.csv > gen_dois.csv
```

Authentication is for [EZID](https://ezid.cdlib.org/), which is where you see the shoulder (that looks like `doi:10.24432/C5`).

If you want to preview the metadata, use `-p`.
If you want to test, remove `-p` and use `doi:10.5072/FK2` as the shoulder.

## Augment JSON

Augment the JSON file with this additional data, might be useful.

Run `augment_accepted.py`, and copy over `accepted_aug.json` to `_data/accepted.json` of the website.