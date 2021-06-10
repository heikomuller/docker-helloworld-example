import argparse
import requests
import sys

from io import StringIO
from pathlib import Path


URLS = [
    'https://www.gutenberg.org/files/3201/files/NAMES-F.TXT',
    'https://www.gutenberg.org/files/3201/files/NAMES-M.TXT'
]


def main(outputfile):
    """
    Download files with popular male and female names and write the combined
    result to the given output file.
    """
    names = list()
    for url in URLS:
        r = requests.get(url)
        r.raise_for_status()
        with StringIO(r.text, newline='') as f:
            names.extend([line.strip() for line in f])
    with outputfile.open('wt') as f:
        for name in names:
            f.write(f"{name}\n")


if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outputfile", required=True)

    parsed_args = parser.parse_args(args)

    main(outputfile=Path(parsed_args.outputfile))
