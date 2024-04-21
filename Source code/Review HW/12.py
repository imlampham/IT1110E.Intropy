n = int(input())
def sum_of_digits(n):
   sum = 0
   while n > 0:
      digit = n % 10 #lay chu so cuoi cung ra de cong vao sum
      sum += digit
      n //= 10 #bo chu so cuoi cung
   return sum
res = sum_of_digits(n)
print(res)
   