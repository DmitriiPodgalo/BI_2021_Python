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
    return np.array(m1).dot(np.array(m2))


def multiplication_check(m):
    m = np.array(m)
    shapes_m = np.array(list(map(np.shape, m)))
    rows = shapes_m[:, 0][1:]
    cols = shapes_m[:, 1][:-1]
    sum_ = (rows - cols).sum()
    
    if sum_ == 0:
        return True
    else:
        return False


def multiply_matrices(m):
    m = np.array(m)
    temp_matrix = np.array(m)[0]

    if multiplication_check(m):
        for i in range(1, len(m)):
            temp_matrix *= m[i]
        return temp_matrix
    else:
        return None


def compute_2d_distance(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    return np.sqrt(((m2 - m1) ** 2).sum())


def compute_multidimensional_distance(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    return np.sqrt(((m2 - m1) ** 2).sum())


def compute_pair_distances(m):
    m = np.array(m)
    m_out = np.zeros((m.shape[0], m.shape[0]))

    for i in range(m.shape[0]):
        for j in range(i, m.shape[0]):
            m_out[i][j] = compute_multidimensional_distance(m[i], m[j])
            m_out[j][i] = compute_multidimensional_distance(m[i], m[j])

    return m_out
