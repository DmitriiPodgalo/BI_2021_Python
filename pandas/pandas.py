#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:01:05 2022

@author: dmitriipodgalo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv'
df = pd.read_csv(url)

## 1

sns.histplot(df.loc[:,'A':'G'])

## 2

cols = ['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']
df.loc[df['matches'] > df['matches'].mean(), cols].to_csv('train_part.csv', index=None)

## 3

df.head()
df.info()
df.dtypes

cols = ['matches', 'mismatches', 'deletions', 'insertions']
for col in cols:
    sns.histplot(df[col])
    plt.show()
    
sns.heatmap(df.corr())