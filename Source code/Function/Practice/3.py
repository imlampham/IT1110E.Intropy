import math
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False       
    return True
    #kiểm tra số nguyên tố         
    
def print_prime(n):
    for i in range(2, n):
            if prime(i):
                print(i, end = ' ')
    #in toàn bộ số nguyên tố nhỏ hơn n       
    

    
