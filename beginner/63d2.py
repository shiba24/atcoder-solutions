# -*- coding: utf-8 -*-
import numpy as np

N, A, B = map(int, raw_input().split())
h = np.zeros((N, ), dtype=np.int64)
for i in range(N):
    h[i] = input()


def last(h, A, B):
    max_arg = np.argmax(h)
    min_count = h[max_arg] // A
    if min_count == 0:
        min_count += 1
    h[max_arg] -= (A - B) * min_count
    h -= B * min_count
    return h, min_count


count = 0
while np.any(h > 0):
    h, cnt = last(h, A, B)
    count += cnt

print count


# m tosuru

base = A - B

m = np.max(h) / A
h -= base * m
h // 







