#!/usr/bin/env python3

import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    return parser.parse_args()


def main():
    args = parser()
    file = open(args.file).read()
    print(file, end='')


main()
        