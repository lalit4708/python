def common_list(list1,list2):
    new_list = []
    for i in list1:
        if i in list2:
            new_list.append(i)
    return new_list

list1 = [1,2,3,4,5,6]
list2 = [2,4,6,8]

print(common_list(list1,list2))