# def even(a):
#     new_list = []
#     for i in a:
#         if i%2==0:
#             new_list.append(i)
#     return new_list

# num = [1,2,3,4,5,6,7,8,9,10]
# print(even(num))

num = [1,2,3,4,5,6,7,8,9,10]
new_list = set(filter(lambda a:a%2==0,num))
print(new_list)