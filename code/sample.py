import argparse
import sys

from pathlib import Path
from random import Random


def main(inputfile, outputfile, sample_size=10, random_state=None):
    """
    Take a sample of names from a given input file.

    Expects an input file where each line represents a name. the selected sample
    is written to to output file.
    """
    # Read list of names from the input file.
    with inputfile.open('rt') as f:
        names = [line.strip() for line in f]
    # Create random sample of size sample_size.
    rand = Random()
    rand.seed(random_state)
    sample = rand.sample(names, k=sample_size)
    # Write selected sample to output file.
    with outputfile.open('wt') as f:
        for name in sample:
            f.write(f'{name}\n')


if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputfile", required=True)
    parser.add_argument("-o", "--outputfile", required=True)
    parser.add_argument("-r", "--rand", required=False)
    parser.add_argument("-s", "--size", default=10, type=int, required=False)

    parsed_args = parser.parse_args(args)

    main(
        inputfile=Path(parsed_args.inputfile),
        outputfile=Path(parsed_args.outputfile),
        sample_size=parsed_args.size,
        random_state=parsed_args.rand
    )
