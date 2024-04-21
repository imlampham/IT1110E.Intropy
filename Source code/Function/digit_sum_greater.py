def sum_of_digits(a):
    res = 0
    while a > 0:
        digit = a % 10
        res += digit
        a //= 10
    return res

def digit_sum_greater(a,b):
    if sum_of_digits(a) > sum_of_digits(b):
        return 'YES'
    else: 
        return 'NO'