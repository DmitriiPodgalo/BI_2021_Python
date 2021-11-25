import random
import time
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import re


# 1 task
def first_task():
    random_times = {}
    np_times = {}

    for i in range(1, 1001):
        start = time.time()
        for _ in range(i):
            random.uniform(0, 1)
        stop = time.time()

        random_times[i] = stop - start

    for i in range(1, 1001):
        start = time.time()
        np.random.uniform(size=i)
        stop = time.time()

        np_times[i] = stop - start

    xs_random = random_times.keys()
    ys_random = np.array(list(random_times.values())) * (10 ** 6)
    xs_np = np_times.keys()
    ys_np = np.array(list(np_times.values())) * (10 ** 6)

    plt.plot(xs_random,
             ys_random,
             color='#D14139',
             label='random')
    plt.plot(xs_np,
             ys_np,
             color='#1D2DD8',
             label='numpy')

    plt.title('Comparison random and numpy packages')
    plt.xlabel('Times')
    plt.ylabel('Microseconds')

    plt.legend()
    plt.grid()
    plt.show()
    plt.close()


# 2 task
def is_sorted(list_):
    return all(list_[i] <= list_[i + 1] for i in range(len(list_) - 1))


def monkey_sort(list_):
    while (is_sorted(list_) is False):
        np.random.shuffle(list_)


def times():
    times = defaultdict(list)

    for size in range(2, 10):
        for _ in range(1, 6):
            list_ = np.random.normal(size=size)

            start = time.time()
            monkey_sort(list_)
            stop = time.time()

            times[size].append(stop - start)

    xs = times.keys()
    y_means = np.array(list(np.array(times[i]).mean() for i in xs))
    y_sd = np.array(list(np.array(times[i]).std() for i in xs))

    plt.errorbar(xs, y_means, y_sd, marker='^', linestyle='None')

    plt.title('Comparison monkey sort')
    plt.xlabel('List length')
    plt.ylabel('Seconds')

    plt.show()
    plt.close()


# 3 task
def random_walk(steps=100):
    random_steps = np.vstack((np.array([0, 0]),
                              np.random.normal(size=(steps, 2))))
    xs = random_steps[:, 0].cumsum()
    ys = random_steps[:, 1].cumsum()

    plt.plot(xs, ys)
    plt.title('Random walk')
    plt.show()
    plt.close()


# 4 task
def sierpinski_triangle():
    A = np.array([50, 100])
    B = np.array([0, 0])
    C = np.array([100, 0])
    cur_point = np.random.uniform(0, 100, size=2)
    points = np.vstack((A, B, C, cur_point))

    for _ in range(10000):
        chosen_idx = np.random.randint(0, 3)
        cur_point = cur_point + (points[chosen_idx] - cur_point) / 2
        points = np.vstack((points, cur_point))

    xs = points[:, 0]
    ys = points[:, 1]

    plt.scatter(xs, ys)
    plt.title('Sierpinski triangle')
    plt.show()
    plt.close()


# 5 task
def garble_word(match):
    first, middle, last = match.groups()
    middle = list(middle)
    np.random.shuffle(middle)

    return first + ''.join(middle) + last


def random_text(text):
    pattern = r'(\b\w)(\w+)(\w\b)'
    return re.sub(pattern, garble_word, text)
