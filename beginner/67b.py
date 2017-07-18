N, K = map(int, raw_input().split())
l = list(map(int, raw_input().split()))

l.sort(reverse=True)

print sum(l[:K])

