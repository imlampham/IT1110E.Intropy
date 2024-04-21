def is_perfect(n): 
    def sum_div(n): 
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum
    #tính tổng các ước số dương của n
    if n == sum_div(n):
        return True
    else: 
        return False
    '''
    kiểm tra xem tổng đó có bằng số ban đầu n hay không
    nếu có -> perfect number
    '''