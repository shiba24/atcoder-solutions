import numpy as np

h, w = map(int, raw_input().split())
N = int(raw_input())
l = np.array(map(int, raw_input().split()))

z = np.zeros((h * w, ), dtype=np.int64)

c = 0
for i in range(0, N):
    z[c:c + l[i]] = i + 1
    c += l[i]

for k in range(0, h):
    if k % 2 == 0:
        print str(z[k * w:k * w + w])[1:-1]
    else:
        print str(z[k * w:k * w + w][::-1])[1:-1]

