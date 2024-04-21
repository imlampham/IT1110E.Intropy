s = input()
a = s.split('_') #tách chuỗi thành một list nối bằng "_"
for word in a:
    print(word.capitalize(), end = '')
    