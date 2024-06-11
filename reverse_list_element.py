def reverse_element(name):
    list = []
    for element in range(1,len(name)+1):
        for i in range(1,len(element)+1):
            poped_list = name.pop()
            list.append(poped_list)
    return name

name = ["abc","def","ijk"]
new_list = reverse_element(name)
print(new_list)