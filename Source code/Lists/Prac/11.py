import string
lowercases = string.ascii_lowercase

n = int(input())
s = input()

num_char = {}
char_num = {}
for num, ele in enumerate(lowercases):
    num_char[num] = ele
    char_num[ele] = num
#duyệt qua từng ptử ele và chỉ số num của chuỗi lowercases
print(''.join([char if char not in lowercases else \
        num_char[(char_num[char] + n) % 26]  for char in s]))
'''
-Nếu char không nằm trong lowercases, giữ nguyên ký tự đó
-Nếu char là 1 ký tự thường, thực hiện dịch chuyển slg n 
 và lấy ký tự t/ư từ num_char bằng (char_num[char] + n) % 26 
   -> quay lại vị trí ban đầu nếu vượt quá pvi 26 ký tự trong lowercases
''' 