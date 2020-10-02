import requests
import sys
import os
import re

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <reference file>.bib")

    if not os.path.isfile(sys.argv[1]):
        print(f"Not a valid file: {sys.argv[1]}")

    data = ''
    with open(sys.argv[1], 'r') as f:
        data = f.read()

    matches = re.findall(r'@([A-Z]+){([0-9]+)[},]', data, re.IGNORECASE | re.MULTILINE)
    if matches is None:
        print(f"Nothing to import")
    records = set()
    imports = set()
    for match in matches:
        record, label = match
        if record.lower() == 'import' and label.isdigit():
            imports.add(label)
        else:
            records.add(label)

    append = ''
    for label in imports:
        if label in records:
            continue
        req = requests.get(
            f"https://ieeexplore.ieee.org/rest/search/citation/format?recordIds={label}&download-format=download-bibtex",
            headers={
                'Accept': 'application/json',
                'Referer': 'https://ieeexplore.ieee.org/document/' + label
            }
        )

        req.raise_for_status()
        bibtex = req.json().get('data')
        if bibtex:
            append += bibtex + '\n'
            print(f"Imported {label} from IEEE Xplore")
        else:
            print(f"Failed to import {label} from IEEE Xplore")

    data = re.sub("@IMPORT{[0-9]+}", r'', data)
    data += append
    data = data.replace('\r\n', '\n')
    data = re.sub("@IMPORT{[0-9]+}", r'', data)
    data = re.sub(r"[\n]{3,}", r'\n\n', data)

    with open(sys.argv[1], 'w') as f:
        f.write(data)
