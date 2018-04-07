import numpy as np
q = input()

n = np.zeros((q, 2), dtype=np.int64)
for i in range(0, q):    
    n[i, :] = map(int, raw_input().split())

for i in range(0, q):


    s = n[i, 0] * n[i, 1]
    m = int(np.floor(np.sqrt(s)))

    # print m, s

    if n[i, 0] == n[i, 1]:        #equal
        print m * 2 - 2
    elif m ** 2 == s:         # square
        print m * 2 - 3
    elif m ** 2 < s - m:         # square - 1
        print m * 2 - 1
    else:
        print m * 2 - 2





