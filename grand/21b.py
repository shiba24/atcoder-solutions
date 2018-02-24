import numpy as np


N = int(input())

hole = np.zeros((N, 2))
for i in range (0, N):
    p, q = map(int, input().split())
    hole[i] = [p, q]


print(hole)
count = np.array((N, ))

for i in range(0, 1e1000000):
    for j in range(0, 1e1000000):
        count(check(i, j)) += 1

standardize count
