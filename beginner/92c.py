# -*- coding: utf-8 -*-

#### This is Numpy version
# import numpy as np
# N = input()
# A = np.array(map(int, raw_input().split()))


# A = np.append(np.append([0], A), [0])
# total_sum = 0
# for i in range(0, len(A) - 1):
#     total_sum += np.abs(A[i + 1] - A[i])

# for i in range(1, len(A) - 1):
#     partial_sum = total_sum - np.abs(A[i + 1] - A[i]) - np.abs(A[i] - A[i - 1]) + np.abs(A[i + 1] - A[i - 1])
#     print partial_sum


#### This is no-Numpy version
N = input()
A = map(int, raw_input().split())


A = [0] + A + [0]
total_sum = 0
for i in range(0, len(A) - 1):
    total_sum += abs(A[i + 1] - A[i])

for i in range(1, len(A) - 1):
    partial_sum = total_sum - abs(A[i + 1] - A[i]) - abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i - 1])
    print partial_sum

