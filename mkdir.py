#!/usr/bin/env python3

import os
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir')
    parser.add_argument('-p', action='store_true')

    return parser.parse_args()


def main():
    args = parser()
    dir_ = args.dir
    p = args.p
    if p:
        os.makedirs(dir_)
    else:
        os.mkdir(dir_)


main()
