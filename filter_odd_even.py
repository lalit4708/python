def filter_odd_even(list):
    odd_list = []
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    output = [even_list,odd_list]
    return output

list = [1,2,3,4,5,6,7]
print(filter_odd_even(list))