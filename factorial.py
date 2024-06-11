# Write a python program to find the factorial of number
num = int(input("Enter number "))
fact = 1
for i in range(1,num+1):
    fact = fact*i

print(fact)