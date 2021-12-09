#!/usr/bin/env python3

import sys
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    return parser.parse_args()


def main():
    lines = []

    # if sdtin is not empty
    if not sys.stdin.isatty():
        for line in sys.stdin:
            lines.append(line)
    else:
        args = parser()
        file = args.file

        with open(file) as inf:
            for line in inf:
                lines.append(line)

    print(*sorted(lines), sep='', end='')


main()
