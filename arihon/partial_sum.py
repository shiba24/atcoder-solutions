# n = 4
# a = [1, 2, 4, 7]
# k = 13

# a.sort(reverse=1)   # from max to min

# psum = 0

# for ind in range(0, len(a)):
#     part = a[ind:]
#     for i in part:
#         psum += i
#         if psum > k:
#             pass
#         elif psum == k:
#             print('Yes')
#             exit()
#         else:


N = 4
A = [1, 2, 4, 7]
K = 15

def dfs(i, psum):
    if i == N:
        return psum == K
    elif dfs(i + 1, psum) or dfs(i + 1, psum + A[i]):
        return True
    else:
        return False

if dfs(0, 0):
    print('Yes')
else:
    print('No')


### Lake Counting

LAKE = [['.', 'W', '.', 'W'], ['.', '.', '.', '.']]

def lakeCount(x, y):
    if LAKE[x][y] == 'W':
        LAKE[x][y] = '.'

        



