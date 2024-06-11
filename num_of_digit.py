# Write a program to find number of digit in number
num = 3452
count = 0

while num != 0:
    num //= 10
    print(num)
    count += 1
    print(count)

print("Number of digits: " + str(count))