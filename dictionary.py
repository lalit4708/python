user = {'name':'Lalit','age':24,'fav_tune':['Awakening','Fairy tale']}
# for i,j in user.items():
# #     print(f"Key is {i} value is {j}")
# user['fav_song'] = 'Song1'
# print(user)
more_info = {'name':'Lalit Prajapati','State':'Gujarat'}
user.update(more_info)
# print(user)
# user.pop('age')
# print(user)

num = user.get('fav_tune')
print(num)

# user.clear()
# print(user)

# user['fav_tune'] = ['Awakening']

user_item = user.items()
print(user_item)
# print(type(user_item))
# print(user)
# print(type(user))

# user_val = user.values()
# print(user_val)
# print(type(user_val))
# # print(user.values())
# if 'name' in user:
#     print("Present")
# else:
#     print("Not Present")

# if 'name' in user.keys():
#     print("Present")
# else:
#     print("Not present")

# user = {
#     'name':'Lalit',
#     'age':24,
# }

# user['fav_tune'] = ['Awakening','Fairy tale']
# print(user)
# print(type(user))