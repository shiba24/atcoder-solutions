a, b, c = map(int, raw_input().split())

def any_odd(x, y, z):
    if x % 2 or y % 2 or z % 2:
        return True
    else:
        return False

def exchange(a, b, c):
    new_a = b // 2 + c // 2
    new_b = a // 2 + c // 2
    new_c = a // 2 + b // 2
    return new_a, new_b, new_c


if a == b == c and (a + b + c) % 3 == 0 and not any_odd(a, b, c):
    print -1
else:
    k = 0
    while not any_odd(a, b, c):
        a, b, c = exchange(a, b, c)
        k += 1
    print k

