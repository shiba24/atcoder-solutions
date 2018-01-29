# -*- coding: utf-8 -*-
import numpy as np
N, K = map(int, raw_input().split())
x, y, c = [], [], []

for _ in range(N):
    _x, _y, _c = map(str, raw_input().split())
    _x, _y = int(_x), int(_y)
    if _c == 'W':
        _c = 0
    else:
        _c = 1
    x.append(_x)
    y.append(_y)
    c.append(_c)

mat = np.array([[_x, _y, _c] for _x, _y, _c in zip(x, y, c)], dtype=np.int64) % (2 * K)
print mat


def check_meet(K, mat):
    


max_meet = 0
for i in range(0, 2 * K):
    mat[:, 0] = mat[:, 0] + i
    for j in range(0, 2 * K):
        mat[:, 1] = mat[:, 1] + j

        max_meet = np.max(max_meet, meet)


# print 'No'
