#!/usr/bin/env python3

import sys
import re
import argparse


def parser(STDIN_EMPTY):
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern')

    if STDIN_EMPTY:
        parser.add_argument('file')

    return parser.parse_args()


def main():
    STDIN_EMPTY = sys.stdin.isatty()
    args = parser(STDIN_EMPTY)
    file = open(args.file).readlines() if STDIN_EMPTY else sys.stdin
    pattern = r'{}'.format(args.pattern)
    zero = 0

    for line in file:
        for match in re.finditer(pattern, line):
            start = match.span()[0]
            end = match.span()[1]
            print(line[zero:start], '\033[91m', line[start:end], '\033[0m', sep='',  end='')
            zero = end
        if zero != 0:
            print(line[end:], end='')
            zero = 0


main()

