# def square_list(list):
#     list2 = []
#     for i in range(1,len(list)+1):
#         list2.append(i**2)
#     return list2

# list = [1,2,3,4,5]
# new_list = square_list(list)
# print(new_list)

number = [1,2,3,4,5,6]
square = []
# for i in number:
#     square.append(i**2)
# print(square)

square = [x**2 for x in number]
print(square)