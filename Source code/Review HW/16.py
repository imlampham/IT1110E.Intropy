#a = int(input())
#b = int(input())
def sum_of_digits(n):
   sum = 0
   while n > 0:
      digit = n % 10
      sum += digit
      n //= 10
   return sum

def digit_sum_greater(a, b):
   if sum_of_digits(a) > sum_of_digits(b):
      return 'YES'
   return 'NO'
#ans = digit_sum_greater(a, b)
#print(ans) 