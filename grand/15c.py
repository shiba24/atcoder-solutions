import numpy as np

n, m, q = map(int, raw_input().split())

arr = np.zeros((n, m), dtype=np.int32)
Q = np.zeros((q, 4), dtype=np.int32)

for i in range(0, n):
    arr[i] = [int(k) for k in raw_input()]

for i in range(0, q):
    Q[i] = map(int, raw_input().split())

# n, m, q = map(int, raw_input().split())

def count_junction(field):
    a, b = np.where(arr == 1)
    cnt = 0

    def dfs(x, y):
        # field[x][y] = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and field[nx][ny] == 1):
                    dfs(nx, ny)

    for i, j in zip(a, b):
        if (field[i][j] == 1):
            dfs(i, j)
            lake_count += 1
    return lake_count

for qs in Q:
    A = arr[qs[0] - 1:qs[2], qs[1] - 1:qs[3]]
    print count_junction(A)
    # print A
