n = int(input())
def hanoi_tower():
   def transfer(n, start, mid, end):
      if n == 1:
         nonlocal count
         count += 1
      else:
         transfer(n - 1, start, mid, end)
         transfer(1, start, end, mid)
         transfer(n - 1, mid, end, start)
   count = 0 
   transfer(n, 'start', 'end', 'mid')
   return(count)
print(hanoi_tower())

   