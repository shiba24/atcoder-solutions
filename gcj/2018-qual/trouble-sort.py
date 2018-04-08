# -*- coding: utf-8 -*-
# import numpy as np
T = input()

tests = [[]]


for i in range(0, T):

    tests.append()


a, b, k = map(int, raw_input().split())

if a + 2 * k - 2 >= b:
    for i in range(a, b + 1):
        print i
else:
    for i in range(a, a + k):
        print i
    for i in range(b - k + 1, b + 1):
        print i

