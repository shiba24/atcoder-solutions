n, a, b = map(int, raw_input().split())

if n == 1 and a == b:
    print 1
elif n < 2:
    print 0
elif a > b:
    print 0
else:
    print (n - 2) * (b - a) + 1

