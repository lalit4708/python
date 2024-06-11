def decorator_func(any_func):
    def wrapper_fun(*args,**kwargs):
        print("This is awesome function")
        any_func(*args,**kwargs)
    return wrapper_fun

@decorator_func
def func1(a):
    print(f"This is function1 with {a} argument")

func1(6)

# @decorator_func
# def sum(a,b):
#     return a+b

# print(sum(2,3))