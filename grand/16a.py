import numpy as np
alphabet = 'abcdefghijklmnopqrstuvwxyz'

n = raw_input()
N = len(n)


count_dict = {al: n.count(al) for al in alphabet}    

max(np.array(count_dict.values()))








