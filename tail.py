#!/usr/bin/env python3

import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-n', nargs='?', const='10', type=int)

    return parser.parse_args()


def main():
    args = parser()
    file = open(args.file).readlines()
    n = 10 if args.n is None else args.n
    lines = len(file)
    index = 0 if lines - n < 0 else lines - n
    print(*file[index:], sep='', end='')


main()