#!/usr/bin/env python3

import sys
import re
import argparse


def main():
    STDIN_EMPTY = sys.stdin.isatty()
    args = parser(STDIN_EMPTY)
    file = open(args.file).readlines() if STDIN_EMPTY else sys.stdin

    lines, words, characters = counter(args, file)
    print_counter(args, lines, words, characters)


def parser(STDIN_EMPTY):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lines', help='lines count', action='store_true')
    parser.add_argument('-w', '--words', help='words count', action='store_true')
    parser.add_argument('-c', '--characters', help='characters count', action='store_true')

    if STDIN_EMPTY:
        parser.add_argument('file')

    return parser.parse_args()


def words_count(line):
    pattern = r'\b\w+\b'
    return len(re.findall(pattern, line))


def counter(args, file):
    lines = 0
    words = 0
    characters = 0

    for line in file:
        if not (args.lines or args.words or args.characters):
            lines += 1
            words += words_count(line)
            characters += len(line)
        if args.lines:
            lines += 1
        if args.words:
            words += words_count(line)
        if args.characters:
            characters += len(line)

    return lines, words, characters


def print_counter(args, lines, words, characters):
    print_list = []

    if not (args.lines or args.words or args.characters):
        print(lines, words, characters, sep='\t')
        return

    if args.lines:
        print_list.append(lines)
    if args.words:
        print_list.append(words)
    if args.characters:
        print_list.append(characters)

    print(*print_list, sep='\t')


main()
