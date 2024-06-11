# def square(a):
#     new_num = []
#     for i in a:
#         new_num.append(i**2)
#     return new_num

# num = [1,2,3,4,5,6]
# print(square(num))

# num = [1,2,3,4,5,6]
# square = list(map(lambda a:a**2,num))
# print(square)

# def length(a):
#     new_list = []
#     for i in a:
#         new_list.append(len(i))
#     return new_list

# name = ['Lalit','Vishal','Khushal','Vijesh']
# print(length(name))

name = ['Lalit','Vishal','Khushal','Vijesh']
new_list = list(map(lambda a:len(a),name))
print(new_list)
