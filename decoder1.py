# Method 1
# def square(a):
#     new_list = []
#     for i in a:
#         new_list.append(i**2)
#     return new_list

# list = [1,2,3,4,5]
# print(square(list))

# Method 2
# def square(a):
#     return a**2

# list1 = [1,2,3,4,5]
# print(list(map(lambda a:a**2,list1)))

# Method3
# list1 = [1,2,3,4,5]
# def square(a):
#     return a**2

# def my_map(func,l):
#     new_list = []
#     for i in l:
#         new_list.append(func(i))
#     return new_list

# print(my_map(square,list1))

# Function returning function
def outer_func(new_function):
    def inner_func():
        print("This is inner function")
        new_function()
    return inner_func

@outer_func
def func1():
    print("This is function1")

func1()
# # Decoder
# def decoder_function(any_function):
#     def wrapper_function():
#         print("This is good function")
#         any_function()
#     return wrapper_function

# @decoder_function
# def func1():
#     print("This is function1")

# func1()

# var = decoder_function(func1)
# var()
# def func2():
#     print("This is function2")

# # print(func2())
# # This is awesome function
# # This is function1
# def decoder_function(first_function):
#     def wrapper_function(*args,**kwargs):
#         print("This is awesome function")
#         return first_function(*args,**kwargs)
#     return wrapper_function

# @decoder_function
# def sum(a,b):
#     return a+b

# print(sum(3,5))

# @decoder_function
# def function(a):
#     print(f"This is function with {a} argument")

# function(5)
# @decoder_function
# def function1():
#     print("This is function1")

# @decoder_function
# def function2():
#     print("This is function2")

# function1()
# function2()