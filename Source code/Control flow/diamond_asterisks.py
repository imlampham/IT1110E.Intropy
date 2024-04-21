n = int(input())

for i in range(1, n + 1):
    spaces = n - i
    asterisks = 2 * i -1
    line = ' ' * spaces + '*' * asterisks
    print(line)

for i in range(n + 1, 2 * n):
    spaces = i - n
    asterisks = 2 * (2 * n - i) - 1
    line = ' ' * spaces + '*' * asterisks
    print(line)