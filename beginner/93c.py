# -*- coding: utf-8 -*-
# import numpy as np
N = map(int, raw_input().split())
N.sort()

a,b,c = tuple(N)
cnt = 0
d1 = c - a
d2 = c - b

i = d1 / 2
d1 = d1 - i * 2

cnt += i

j = d2 / 2
d2 = d2 - j * 2

cnt += j

if d1 == d2 == 0:
    print cnt

elif d1 == d2 == 1:
    print cnt + 1
else:
    print cnt + 2


