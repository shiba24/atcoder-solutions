N = input()

def total(n):    
    t = 0
    for i in n:
        t += int(i)
    return t

if len(N) == 1:
    print(N)
else:
    if N[1:] == '9' * (len(N) - 1):
        print(total(N))
    else:
        print(total(str(int(N[0]) - 1) + '9' * (len(N) - 1)))
