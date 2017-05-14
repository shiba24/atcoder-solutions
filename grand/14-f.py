N = input()
p = map(int, raw_input().split())

def strangesort(arr):
    high = [i for index, i in enumerate(arr) if i >= max(arr[:index + 1])]
    other = [i for index, i in enumerate(arr) if i < max(arr[:index + 1])]
    return other + high


count = 0
while p != range(1, N + 1):
    p = strangesort(p)
    count += 1

print count 


