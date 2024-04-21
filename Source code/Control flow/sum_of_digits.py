n = int(input())
def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10 #lay chu so cuoi cung cua n
        sum += digit
        n //= 10 #xoa chu so cuoi cung cua n
    return sum
total = sum_of_digits(n)
print(total)