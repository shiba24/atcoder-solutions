# -*- coding: utf-8 -*-
import numpy as np
N = input()
A1 = np.array(map(int, raw_input().split()))
A2 = np.array(map(int, raw_input().split()))
A = np.array([A1, A2], dtype=np.int32)

# df = - 1 * np.diff(A, axis=0)[0]
# # print A.shape, len(df)
# max_col = np.zeros(len(df))
# all_sum = np.sum(df)

# for i in range(0, len(df)):
#     sum_i = np.sum(df[:i + 1])
#     # rest_i = all_sum - sum_i
#     rest_i = np.sum(df[i:])
#     max_col[i] = sum_i - rest_i
#     # print df, sum_i, rest_i

# down = np.argmax(max_col)
# # print max_col, down, np.sum(A[0, :down + 1]) + np.sum(A[1, down:])
# print np.sum(A[0, :down + 1]) + np.sum(A[1, down:])

max_sum = 0
for i in range(0, len(A[0])):
    # print A[0, :i + 1], A[1, i:]
    max_sum = np.max([max_sum, np.sum(A[0, :i + 1]) + np.sum(A[1, i:])])

print max_sum

