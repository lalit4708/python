def total(*args):    # *args = 3,4,5,6
    sum = 0
    for i in args:
        sum = sum + i
    return sum

list = [3,4,5,6]
print(total(*list))