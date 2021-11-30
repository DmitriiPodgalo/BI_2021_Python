#!/usr/bin/env python3

import os
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help='show all files', action='store_true')
    parser.add_argument('dir_name', nargs='?', const='.', type=str)

    return parser.parse_args()


def main():
    args = parser()
    dir_name = '.' if args.dir_name is None else args.dir_name
    files = os.listdir(dir_name)

    if args.all:
        for file in files:
            print(file)
    else:
        for file in files:
            if file[0] != '.':
                print(file)


main()
