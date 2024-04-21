def reverse_string(s):
    if len(s) == 1: 
        return s
    return s[len(s) - 1] + reverse_string(s[0 : (len(s) - 1)])

'''
Write a recursive function reverse_string(str) to reverse a given string.
test: print(reverse_string('Bach khoa'))
result: aohk hcaB
'''