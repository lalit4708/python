def str_rev(name):
    index = len(name)
    rstr = ""
    while index>0:
        rstr += name[index -1]
        index -= 1
    return rstr


name = input("ENTER YOUR NAME ")
reverse = str_rev(name)
print(reverse)