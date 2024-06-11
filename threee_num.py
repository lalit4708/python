a = int(input("ENTER FIRST NUMBER "))
b = int(input("ENTER FIRST NUMBER "))
c = int(input("ENTER FIRST NUMBER "))

# if a>b and a>c:
#     print("A IS GREATER")
# elif b>a and b>c:
#     print("B IS GREATER")
# else:
#     print("C IS GREATER")

if a>b:
    if a>c:
        print("A IS GREATER")
    else:
        print("C IS GREATER")
else:
    if b>c:
        print("B IS GREATER")
    else:
        print("C IS GREATER")