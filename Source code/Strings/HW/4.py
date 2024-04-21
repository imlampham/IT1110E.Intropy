def is_palindrome(s):
    s = s.replace(' ', '')
    # print(s)
    if s[0] != s[len(s) - 1]:
        return 'NO'
    if s == '' or len(s) == 1:
        return 'YES'
    return is_palindrome(s[1: len(s) - 1])

'''
Given a string, write a recursive function is_palindrome(str) to check if it is palindrome or not. The function returns 'YES' if the input string is palindrome. Otherwise, the function returns 'NO'. 
A string is said to be palindrome if the reverse of the string is the same as string, where spaces are ignored. 
'''