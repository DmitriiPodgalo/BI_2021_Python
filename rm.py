#!/usr/bin/env python3

import os
import shutil
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store_true')
    parser.add_argument('path')

    return parser.parse_args()


def main():
    args = parser()
    path = args.path
    r = args.r

    remove(path, r)


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def remove(path, r):    
    if is_file(path):
        os.remove(path)
    elif is_dir(path) and r:
        shutil.rmtree(path)
    elif is_dir(path):
        os.removedirs(path)

main()
