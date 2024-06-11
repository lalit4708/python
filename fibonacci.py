# Write a python program to print fibonacci series
fnum = int(input("Enter first number "))
snum = int(input("Enter second number"))

for i in range(1,11):
    tnum = fnum + snum
    fnum = snum
    snum = tnum
    print(tnum)