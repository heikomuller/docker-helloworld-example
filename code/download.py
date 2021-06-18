import argparse
import requests
import sys

from pathlib import Path


URL_ALL = 'https://www.gutenberg.org/files/3201/files/NAMES.TXT'
URL_FEMALE = 'https://www.gutenberg.org/files/3201/files/NAMES-F.TXT'
URL_MALE = 'https://www.gutenberg.org/files/3201/files/NAMES-M.TXT'


def main(outputfile, gender=None):
    """
    Download files with popular male and female names to the given output file.
    """
    if gender == 'female':
        url = URL_FEMALE
    elif gender == 'male':
        url = URL_MALE
    else:
        url = URL_ALL
    r = requests.get(url)
    r.raise_for_status()
    print(f"Download {url} to {outputfile}")
    with outputfile.open('wt') as f:
        f.write(r.text)


if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gender", required=False)
    parser.add_argument("-o", "--outputfile", required=True)

    parsed_args = parser.parse_args(args)

    main(outputfile=Path(parsed_args.outputfile), gender=parsed_args.gender)
