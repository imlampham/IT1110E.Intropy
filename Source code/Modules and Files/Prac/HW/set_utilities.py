def set_union(A, B):
    uni_set = set(A)
    for ele in B:
        uni_set.add(ele)
    return uni_set

def set_intersection(A, B):
    intersect_set = set()
    for ele in A:
        if ele in B:
            intersect_set.add(ele)
    return intersect_set
