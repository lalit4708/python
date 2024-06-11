def list_reverse(name):
    new_list = []
    for i in range(1,len(name)+1):
        poped_item = name.pop()
        new_list.append(poped_item)
    return new_list


name = ["Lalit", "Vijesh", "Vishal", "Darshan"]
print(list_reverse(name))

