def sum_of_digit(n):
    sum = 0
    while n > 0:
        digit = n % 10 #lay chu so cuoi cung cua n
        sum += digit
        n //= 10 #xoa chu so cuoi cung cua n
    return sum
