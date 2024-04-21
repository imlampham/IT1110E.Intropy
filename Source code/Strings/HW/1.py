def check(s):
    count = 0
    for i in range(4):
        if s[i].isupper():
            count += 1
            if count == 2:
                return True
    return False

def to_uppercase(s):
    return s.upper() if check(s) else s

'''
Write a function to_uppercase(str) to convert a given string to all uppercase 
if it contains at least 2 uppercase characters in the first 4 characters.
'''