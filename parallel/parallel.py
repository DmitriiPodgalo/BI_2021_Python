#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:24:00 2022

@author: dmitriipodgalo
"""

from Bio import SeqIO
from collections import Counter
import argparse
from concurrent.futures import ProcessPoolExecutor


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fasta', type=str)
    parser.add_argument('-t', '--threads', default=1, type=int)
    
    return parser.parse_args()


def reader(path, threads):
    with open(path) as inf, ProcessPoolExecutor(threads) as pool:
        for record in SeqIO.parse(inf, 'fasta'):
            pool.submit(counter, record)


def counter(record):
    counts = Counter(record.seq)

    print('Contig', record.name[1:].split()[0] + ':', end=' ')
    print(', '.join('{}={}'.format(k, v) for k, v in counts.items()))


if __name__ == '__main__':
    args = parser()
    reader(path=args.fasta, threads=args.threads)