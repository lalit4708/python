# user_id = ['user1','user2','user3']
# name = ['Lalit','Vishal','Khushal']
# age = [23,24,34]

# print(list(zip(user_id,name,age)))
new_list = [('user1', 'Lalit', 23), ('user2', 'Vishal', 24), ('user3', 'Khushal', 34)]
user_id, name, age = list(zip(*new_list))
print(user_id)
print(name)
print(age)