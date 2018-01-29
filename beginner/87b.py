# -*- coding: utf-8 -*-
a = input()
b = input()
c = input()
x = input()

max_a = x / 500

count = 0
# print max_a
for i in range(0, min(a, max_a) + 1):
    rest = x - i * 500
    max_b = rest / 100
    # print rest, max_b
    for j in range(0, min(b, max_b) + 1):
        rest_c = rest - j * 100
        if rest_c <= c * 50:
            count += 1

print count
