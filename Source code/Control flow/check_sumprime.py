n = int(input())

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0,5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(n):
    number = int(input())
    found = False

    for j in range(2, number // 2 + 1):
        if check_prime(i) and check_prime(number - i):
            found = True
            break

if found:
    print('YES')
else: 
    print('NO')
