n = int(input())
def calculate():
   if n <= 1:
      return n
   
   a_minus_2 = 0
   a_minus_1 = 1
   
   for i in range(2, n + 1):
      a_i = 2 * a_minus_1 + a_minus_2
      a_minus_2, a_minus_1 = a_minus_1, a_i
   return a_i
res = calculate()
print(res)