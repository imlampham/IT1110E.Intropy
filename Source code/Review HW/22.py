'''
x = int(input())
y = int(input())
z = int(input())
def find_mid(x, y, z):
   :
      return y
   elif (y <=x and x <= z) or (y >= x and x >= z):
      return x
   return z

mid = lambda x, y, z: x if find_mid(x, y, z) == x else \
                        y if find_mid(x, y, z) == y else \
                           z
print(mid(x, y, z))
'''
mid = lambda x, y, z: x if (y <= x and x <= z) or (y >= x and x >= z) else \
                     y if (x <= y and y <= z) or (x >= y and y >= z) else \
                        z
