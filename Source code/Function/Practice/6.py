def dec_to_bin(n):
    return str(bin(int(n)))[2:]
'''
- truyền giá trị int(n) để chuyển đổi số nguyên n thành chuỗi số nhị phân
- dùng str() để chuyển kqua thành chuỗi
- sử dụng [2:] để cloại bỏ hai ký tự đầu tiên (0b) của chuỗi số nhị phân
'''