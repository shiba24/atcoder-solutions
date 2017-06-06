# -*- coding: utf-8 -*-
import numpy as np

N = input()
s = np.zeros((N, ), dtype=np.int32)
for i in range(N):
    s[i] = input()


s.sort()
largest_s = np.sum(s)

if largest_s % 10 != 0:
    print largest_s
    exit()

for i in range(N):
    if (largest_s - s[i]) % 10 != 0:
        print largest_s - s[i]
        exit()
print 0

