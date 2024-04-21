tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])

res = [[j for j in range(i, i+n)] for i in range(1, m*n, n)]
'''
Với mỗi gtrị i trong khoảng từ 1 đến m*n-1 (step = n), 
tạo 1 ds con trong đó các ptử là các số nguyên từ i đến i+n-1
-> Matrix với m hàng, n cột
'''
for line in res:
    print(*line)