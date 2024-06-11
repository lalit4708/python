def sorted_num(a,b,c):
    maximum = max(a,b,c)
    minimum = min(a,b,c)
    middle = (a+b+c) - minimum - maximum
    print(minimum,middle,maximum)

a = int(input("ENTER FIRST NUMBER "))
b = int(input("ENTER SECOND NUMBER "))
c = int(input("ENTER THIRD NUMBER "))

sorted_num(a,b,c)
# print(sorted_num(a,b,c))



