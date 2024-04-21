n = int(input())
def fibonacci_sequence():
   if n <= 1:
      return n
   
   f_minus_2 = 0
   f_minus_1 = 1
   
   for i in range(2, n + 1):
      f_i = f_minus_1 + f_minus_2
      f_minus_2, f_minus_1 = f_minus_1, f_i
   return f_i
res = fibonacci_sequence()
print(res)
   
