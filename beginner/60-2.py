# -*- coding: utf-8 -*-
a, b, c = map(int, raw_input().split())
check = 0
while check <= a:
    if (b * check + c) % a == 0:
        print "YES"
        exit()
    check += 1
print "NO"


