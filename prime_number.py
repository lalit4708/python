num = int(input("ENTER NUMBER "))
flag = 0
i = num
while i >= 1:
    if num%i==0:
        flag = flag + 1
    i=i-1
    
if(flag == 2):
    print("ENTERED NUMBER IS PRIME")
else:
    print("ENTERED NUMBER IS NOT PRIME")