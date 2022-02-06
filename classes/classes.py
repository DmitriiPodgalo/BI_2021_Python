#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:30:26 2022

@author: dmitriipodgalo
"""


from Bio.Seq import Seq
from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib


class Game():

    muscle = 8
    brain = 5
    is_pet = False

    def __init__(self, name='Knight', age=21):
        self.name = name
        self.coef_age = age ** 0.5

    def gym(self):
        self.muscle += (0.01 * (100 - self.coef_age))

    def read(self):
        self.brain += (0.005 * ((100 - self.coef_age)))

    def watch_TV(self):
        self.brain -= (0.01 * self.coef_age)

    def lay(self):
        self.muscle -= (0.01 * self.coef_age)
        self.brain -= (0.005 * self.coef_age)

    def pet(self):
        if self.is_pet:
            print(self.name + ', this good for you')
        elif self.brain + self.muscle > 50:
            self.is_pet = True
            print(self.name + ', congrans, now you have a pet')
        else:
            print(self.name + ', sorry...')


class RNA():

    def __init__(self, rna):
        self.rna = Seq(rna)

    def translation(self):
        return str(self.rna.translate())

    def back_transcription(self):
        return str(self.rna.back_transcribe())


class MySet(set):

    def __init__(self, set_):
        if sum(i < 0 for i in set_):
            raise ValueError('Have negative item')

        super().__init__(set_)

    def add(self, item):
        if item > 0:
            super(MySet, self).add(item)


class FastAnalyse():

    def __init__(self, path):
        self.reads = []
        for record in SeqIO.parse(path, 'fasta'):
            self.reads.append(record.seq)

    def counter_reads(self):
        return len(self.reads)

    def hist_len(self):
        reads_len = list(sorted(map(len, self.reads)))
        sns.histplot(reads_len)
        plt.title('Length distribution')

    def counter_gc(self):
        counter = 0
        sum_ = sum(map(len, self.reads))
        for read in self.reads:
            counter += read.count('G') + read.count('C')

        return (str(round(counter / sum_ * 100, 2)) + '%')


    def counter_4mer(self):

        dict_ = {}

        for read in self.reads:
            for letter in range(len(read) - 4):
                end = letter + 4
                mer = str(read[letter:end])

                if mer in dict_.keys():
                    dict_[mer] += 1
                else:
                    dict_[mer] = 1

        dict_ = {k: v for k, v in sorted(dict_.items(), key=lambda x: x[1], reverse=True)}

        plt.bar(dict_.keys(), dict_.values())
        plt.gca().margins(x=0)
        plt.gcf().canvas.draw()
        tl = plt.gca().get_xticklabels()
        maxsize = max([t.get_window_extent().width for t in tl])
        m = 0.2
        s = maxsize / plt.gcf().dpi * len(dict_) + 2 * m
        margin = m / plt.gcf().get_size_inches()[0]
        plt.gcf().subplots_adjust(left=margin, right=1 - margin)
        plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
        plt.xticks(rotation=90)
        plt.title('4-mer distribution')

    def __str__(self):
        return str(pathlib.Path().resolve())

    def summarise(self):
        return self.counter_reads(), self.counter_gc()
