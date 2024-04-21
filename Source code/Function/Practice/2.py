def pline(i):
    def ele(i, j):
        if i == 1 or j == 1 or j == i:
            return 1
        return ele(i - 1, j - 1) + ele(i - 1, j)
    #tính giá trị của phần tử tại vị trí (i,j)

    def loop(j):
        '''if j == 1:
            print(' ', end = '')'''
        print(ele(i,j), end = ' ')
        if j != i:
            loop(j+1)
    loop(1)
    print()
    #in các phần tử trên một dòng của tam giác Pascal

def pascal(i, n):
    pline(i)
    if i != n:
        pascal(i+1, n)
    #in tam giác Pascal

def pascal_triangle(n):
    pascal(1, n)
    #in toàn bộ tam giác Pascal với n dòng
