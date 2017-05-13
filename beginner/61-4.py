# -*- coding: utf-8 -*-
def calc_weight(pw, weights):
    new_pw = pw[:]
    k = 0
    for l, (p, w) in enumerate(pw):
        if p != len(weights) - 1:
            li = weights[p]
            non_zero = [[i, x] for i, x in enumerate(li) if x != 0]
            for j, x in non_zero:
                new_pw.append([j, x + w])
            new_pw.pop(l + k)
            k += 1
    return new_pw

# def calc_weight(pw, weights):
#     new_pw = []
#     k = 0
#     for p, w in pw:
#         if p == len(weights) - 1:
#             new_pw.append([p, w])            
#         li = weights[p]
#         non_zero = [[i, x] for i, x in enumerate(li) if x != 0]
#         for j, x in non_zero:
#             new_pw.append([j, x + w])
#     return new_pw

N, M = map(int, raw_input().split())
matrix = [[0 for i in range(N)] for j in range(N)]
for i in range(M):
    _a, _b, _c = map(int, raw_input().split())
    matrix[_a - 1][_b - 1] = _c

cur_pw = [[0, 0]]
for i in range(0, N):
    cur_pw = calc_weight(cur_pw, matrix)

ans = [[i, j] for i, j in cur_pw if i == N - 1]
non_ans = [[i, j] for i, j in cur_pw if i != N - 1]
if non_ans:
    print "inf"
else:
    ans.sort(key=lambda x:x[1], reverse=True)
    print ans[0][1]

