#!/usr/bin/env python3

import sys
import re
import argparse


def main():
    args = parser()
    lines = 0
    words = 0
    characters = 0

    for line in sys.stdin:
        if not (args.lines and args.words and args.characters):
            lines += 1
            words += words_count(line)
            characters += len(line)
        if args.lines:
            lines += 1
        if args.words:
            words += words_count(line)
        if args.characters:
            characters += len(line)

    if args.lines:
        print(lines, end='\t')
    if args.words:
        print(words, end='\t')
    if args.characters:
        print(characters)
    if not (args.lines and args.words and args.characters):
        print(lines, words, characters, end='\t')


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lines', help='lines count', action='store_true')
    parser.add_argument('-w', '--words', help='words count', action='store_true')
    parser.add_argument('-c', '--characters', help='characters count', action='store_true')

    return parser.parse_args()


def words_count(line):
    return len(re.findall(r'\b\w+\b', line))


main()
