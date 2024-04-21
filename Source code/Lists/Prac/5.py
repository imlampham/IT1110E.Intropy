def remove_duplicates(l):
    new_l = list() #tạo list mới chứa các phần tử ko trùng lặp
    first_check = True #check lần đầu lặp qua list
    
    for ele in l:
        if first_check: 
            first_check = False
            pre = ele
            new_l.append(ele) #check có phải là lần đầu lặp qua danh sách 
        else: #nếu không phải lần đầu lặp qua danh sách
            if pre != ele:
                new_l.append(ele)
            pre = ele 
    return new_l

