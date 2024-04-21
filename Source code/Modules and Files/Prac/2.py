import numpy as np

def convert(a):
    sum_all_ele = np.sum(a, axis = 1, keepdims = True)
    return a / sum_all_ele
