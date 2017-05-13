# -*- coding: utf-8 -*-
N, M = map(int, raw_input().split())
a = []
b = []
for _ in range(M):
    _a, _b = map(int, raw_input().split())
    a.append(_a)
    b.append(_b)

ans = [0] * N
for i in range(0, N):
    ans[i] = a.count(i + 1) + b.count(i + 1)

    print ans[i]



