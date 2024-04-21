temp = input().split(' ')
m, n = int(temp[0]), int(temp[1]) 
#gán giá trị các ptử trong temp vào m và n để biểu thị số hàng, cột của ma trận

a = []
b = []
for i in range(m):
    a.append(input().split(' '))
for i in range(m):
    b.append(input().split(' '))
result = [[int(a[i][j]) + int(b[i][j]) for j in range(n)] for i in range(m)]
#tính tổng của từng phần tử tương ứng trong ma trận a và b
for line in result:
    print(*line)