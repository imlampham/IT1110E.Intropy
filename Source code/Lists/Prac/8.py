def dictionary_convert(s):
    d = dict() 
    for char in s:
        d[char] = d.get(char, 0) + 1 
    return d
