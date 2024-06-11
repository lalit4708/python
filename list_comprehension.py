list1 = [1,2,3,4,5]
# [1,4,9,16,25]
# square = []
# for i in list1:
#     square.append(i**2)
# print(square)

# square = [i**2 for i in list1]
# print(square)

list2 = [1,2,3,4,5]
# [-1,-2,-3-,4,-5]
# negative = []
# for i in list2:
#     negative.append(-i)
# print(negative)

# negative = [-i for i in list2]
# print(negative)

names = ['Lalit','Rakesh','Khushal']
# # ['L','R','K']
# new_list = [name[0] for name in names]
# print(new_list)

# numberes = list(range(1,6))
# for i in numberes:
#     if i%2!=0:
#         print(i)
# [1,2,3,4,5]
# [-1,-3,-5]
# [4,8] 

num = [1,2,3,4,5]
# new_list = []
# for i in num:
#     if i%2==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

new_list = [i*2 if(i%2==0) else -i for i in num]
print(new_list)

# num = [i for i in numberes if i%2!=0]
# print(num)

