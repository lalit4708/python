def area_1(r):
    return 3.14 * r *r

def area(a,b):
    return a*b

r = int(input("ENTER VALUE OF RADIUS "))
l = int(input("ENTER VALUE OF LENGTH "))
b = int(input("ENTER VALUE OF BRADTH "))

area1 = area_1(r)
area2 = area(l,b)
print(f"AREA OF CIRCLE IS {area1}")
print(f"AREA OF RECTANGLE IS {area2}")