import argparse
import requests
import sys

from io import StringIO
from pathlib import Path


URL = 'https://www.gutenberg.org/files/3201/files/NAMES.TXT'


def main(outputfile):
    """
    Download files with popular male and female names to the given output file.
    """
    r = requests.get(URL)
    r.raise_for_status()
    with StringIO(r.text, newline='') as f:
        with outputfile.open('wt') as f:
            for name in [line.strip() for line in f]:
                f.write(f"{name}\n")


if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outputfile", required=True)

    parsed_args = parser.parse_args(args)

    main(outputfile=Path(parsed_args.outputfile))
