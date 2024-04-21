s = input()
def is_palindrome(s):
   s = s.replace(' ', '')
   if s == '' or len(s) == 1:
      return 'YES'
   if s[0] != s[len(s) - 1]:
      return 'NO'
   return is_palindrome(s[1:len(s) - 1])
print(is_palindrome(s))
   