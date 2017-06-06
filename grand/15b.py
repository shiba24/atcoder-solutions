n = raw_input()
N = len(n)


db = 0
for cnt, i in enumerate(n):
    if i == "U":
        db += cnt
    elif i == "D":
        db += N - cnt - 1

print N * (N - 1) + db


