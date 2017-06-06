a = raw_input()

a = sorted(a)

for i in range(0, len(a) - 1):
    if a[i] == a[i + 1]:
        print 'no'
        exit()
print 'yes'


