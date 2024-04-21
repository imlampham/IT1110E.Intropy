def substrings_count(s):
    count = 0
    '''
    first = s[0]
    last = s[len(s) - 1]
    #print('   ' + s)
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            if i == j and (s[i] == first or s[i] == last):
                count += 1
                print(str(count) + ') ' + ' ' * i + s[i])
            elif s[i] == first and s[j] == last:
                print(str(count) + ') ' + ' ' * i + s[i: j + 1])
                count += 1
    '''
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                count += 1
    return count
'''
print(substrings_count('aab cb')) = 8
print(substrings_count('hoc python')) = 12
print(substrings_count('toi la sinh vien bach khoa ha noi')) = 78'''

'''
Given a string str, we are interested in its substrings with the same first and last characters. 
Your task is to write a function substrings_count(str) to count the number of such substrings.
'''