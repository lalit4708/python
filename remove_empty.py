# #Remove empty strings 
# name = ["Khushal","","Haresh","Mahesh","","Suresh"]
# res = filter(name,None)
# print(res)
list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(25)
print(index)
# # update item present at location
list1[index] = 200
print(list1)