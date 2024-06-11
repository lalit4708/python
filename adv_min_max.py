# def func(item):
#     return len(item)

# name = ['Lalit','Vishal','Khushal']
# print(min(name, key=func))

student = [
    {'name':'Lalit','score':90,'age':24},
    {'name':'Vishal','score':96,'age':23},
    {'name':'Khushal','score':95,'age':22}
]

print(min(student, key=lambda item:item.get('age'))['name'])