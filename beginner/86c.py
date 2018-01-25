# -*- coding: utf-8 -*-
import numpy as np
N = input()
t, x, y = [0], [0], [0]
for _ in range(N):
    _t, _x, _y = map(float, raw_input().split())
    t.append(_t)
    x.append(_x)
    y.append(_y)

txy = np.array([[_t, _x, _y] for _t, _x, _y in zip(t, x, y)], dtype=np.int32)

dm = np.diff(txy, axis=0)
for d in dm:
    total = np.abs(d[1]) + np.abs(d[2])
    if d[0] >= total and (d[0] - total) % 2 == 0:
        print 'Yes'
        exit()

print 'No'