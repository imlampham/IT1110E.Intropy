valid_chars = {'b':'d', 
               'd':'b', 
               'i':'i', 
               'o':'o', 
               'p':'q', 
               'q':'p', 
               'v':'v', 
               'w':'w', 
               'x':'x'}
#các kí tự tương ứng 

def valid(s):
    for character in s:
        if character not in valid_chars:
            return False
    return True
#kiểm tra từng item trong s có nằm trong valid_chars hay không

def mirror(s):
    if valid(s):
        return ''.join([valid_chars[c] for c in s[::-1]])
    return 'NOT POSSIBLE'
#phép gương của chuỗi s nếu hợp lệ
