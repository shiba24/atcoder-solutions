# -*- coding: utf-8 -*-
N, W = map(int, raw_input().split())
w = []
v = []
for _ in range(N):
    _w, _v = map(float, raw_input().split())
    w.append(_w)
    v.append(_v)

w1 = w[0]

wv = [[_w, _v, _v / _w] for _w, _v in zip(w, v)]
wv.sort(key=lambda x:x[0])
wv.sort(key=lambda x:x[2], reverse=True)
print wv
v_sum = 0
margin = W - 0
for i in range(0, N):
    if wv[i][0] <= margin:
        print wv[i]
        v_sum += wv[i][1]
        margin -= wv[i][0]
print int(v_sum)
