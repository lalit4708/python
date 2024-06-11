# def decorator_fun(any_fun):
#     def wrapper_fun():
#         print("This is awesome function")
#         any_fun()
#     return wrapper_fun

# def fun1():
#     print("This is function 1")

# s = decorator_fun(fun1)
# s()

# Example 2:
def decorator_fun(any_fun):
    def wrapper_fun():
        print("This is awesome function")
        any_fun()
    return wrapper_fun

@decorator_fun
def func1():
    print("This is function 1")

func1()