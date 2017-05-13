# -*- coding: utf-8 -*-
N, T = map(int, raw_input().split())
t = map(int, raw_input().split())
total = 0
for k in range(0, N - 1):
    if t[k + 1] - t[k] <= T:
        total += t[k + 1] - t[k]
    else:
        total += T
total += T
print total
