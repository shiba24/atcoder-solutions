# -*- coding: utf-8 -*-
import numpy as np

N, A, B = map(int, raw_input().split())
h = np.zeros((N, ), dtype=np.int64)
for i in range(N):
    h[i] = input()


def last_two(arr, a, b):
    arr.sort()
    last = np.where(np.diff(arr) > 0)[0]
    if last == []:
        d = arr[last + 1] - arr[last]
        cnt = d // (a - b) + 1
    else:
        cnt = 1
    arr[-1] -= (A - B) * cnt
    arr -= B * cnt
    return np.clip(arr, 0, 1000000000), cnt

count = 0
while np.any(h > 0):
    h, cnt = last_two(h, A, B)
    count += cnt

print count

