#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:28:51 2021

@author: dmitriipodgalo
"""

import numpy as np


if __name__ == "__main__":
    np.array([1, 2, 3])
    np.arange(1, 10, 0.5)
    np.ones(10)


def matrix_multiplication(m1, m2):
    return np.array(m1) * np.array(m2)


def multiplication_check(m):
    m = np.array(m)

    try:
        for i in range(0, len(m) - 1):
            m[i] * m[i + 1]
    except ValueError:
        return False
    else:
        return True


def multiply_matrices(m):
    m = np.array(m)
    temp_matrix = np.array(m)[0]

    try:
        for i in range(1, len(m)):
            temp_matrix *= m[i]
    except ValueError:
        return None
    else:
        return temp_matrix


def compute_2d_distance(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    return np.sqrt((m2[0] - m1[0]) ** 2 + (m2[1] - m1[1]) ** 2)


def compute_multidimensional_distance(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    return np.sqrt(((m2 - m1) ** 2).sum())


def compute_pair_distances(m):
    m = np.array(m)
    m_out = np.zeros((m.shape[0], m.shape[0]))

    for i in range(m.shape[0]):
        for j in range(i, m.shape[0]):
            m_out[i][j] = np.sqrt(((m[i] - m[j]) ** 2).sum())
            m_out[j][i] = np.sqrt(((m[i] - m[j]) ** 2).sum())

    return m_out.astype(int)
