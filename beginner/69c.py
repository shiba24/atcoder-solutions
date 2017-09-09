import numpy as np

N = int(raw_input())
l = np.array(map(int, raw_input().split()))

mod_4 = len(np.where((l % 4 == 0))[0])
mod_2 = len(np.where(l % 4 == 2)[0])

if N <= 2 and mod_4 == 0 and mod_2 <= 1:
    print 'No'
elif N <= mod_4 * 2 + 1:
    print 'Yes'
elif N <= mod_4 * 2 + mod_2 and mod_2 >= 2:
    print 'Yes'
elif N <= mod_4 * 2 + mod_2:
    print 'Yes'
else:
    print 'No'
