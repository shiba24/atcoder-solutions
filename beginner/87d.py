# -*- coding: utf-8 -*-
import numpy as np
N, M = map(int, raw_input().split())
l, r, d = [], [], []

for _ in range(M):
    _l, _r, _d = map(int, raw_input().split())
    l.append(_l)
    r.append(_r)
    d.append(_d)

X = np.zeros((N, ), dtype=np.int64)
is_accessed = np.zeros((N, ), dtype=np.bool)

if M > 0:
    # X[l[0]] = 0
    X[r[0] - 1] = d[0]
    is_accessed[r[0] - 1], is_accessed[l[0] - 1] = True, True
    # print X, is_accessed
    for i in range(1, M):
        if is_accessed[l[i] - 1] and is_accessed[r[i] - 1]:
            if X[r[i] - 1] != X[l[i] - 1] + d[i]:
                print 'No'
                exit()
        # elif is_accessed[r[i] - 1] and not is_accessed[l[i] - 1]:
        elif is_accessed[r[i] - 1]:
            X[l[i] - 1] = X[r[i] - 1] - d[i]
            is_accessed[l[i] - 1] = True
        # elif is_accessed[l[i] - 1] and not is_accessed[r[i] - 1]:
        elif is_accessed[l[i] - 1]:
            X[r[i] - 1] = X[l[i] - 1] + d[i]
            is_accessed[r[i] - 1] = True
        else:
            X[r[i] - 1] = d[i]
            is_accessed[r[i] - 1], is_accessed[l[i] - 1] = True, True
        # print X, is_accessed

if np.max(X) - np.min(X) > 1000000000:
    print 'No'

print 'Yes'
