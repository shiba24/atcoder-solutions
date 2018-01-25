# -*- coding: utf-8 -*-
import numpy as np

a, b = map(str, raw_input().split())
i = int(a + b)

if i == int(np.sqrt(i)) ** 2:
    print "Yes"
else:
    print "No"


