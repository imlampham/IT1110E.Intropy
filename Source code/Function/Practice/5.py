def fibo(n):
    a = [0, 1] #tạo mảng a với 2 giá trị Fibonacci ban đầu
    for i in range(n - 1):
        a.append(None) 
    #phần tử None này sẽ được thay thế bởi giá trị Fibonacci tương ứng sau khi tính toán
    if a[n] is not None:
        return a[n]
    #kiểm tra xem giá trị Fibonacci thứ n đã được tính toán trước đó chưa
    a[n] = fibo(n - 2) + fibo(n - 1) 
    #gán giá trị Fibonacci thứ n bằng tổng của hai số Fibonacci trước đó
    return a[n]