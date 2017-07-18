# import numpy as np
N = input()
# a =  np.araray((map(int, raw_input().split())))
# sum_a = np.sum(a)
a =  list(map(int, raw_input().split()))
sum_a = sum(a)

sum_top = a[0] + 0
sum_bottom = a[-1] + 0
cur_sum = sum_top

for i in range(1, N - 1):
    sum_top += a[i]
    if abs(sum_a / 2. - sum_top) <= abs(sum_a / 2. - cur_sum):
        cur_sum = sum_top

print abs(2 * cur_sum - sum_a)

