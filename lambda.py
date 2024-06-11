sum = lambda a,b:a+b
print(sum(5,6))

# even = lambda a:'even' if a%2==0 else 'odd'
# print(even(6))


num = int(input("ENTER NUMBER "))
numbers = lambda a:'Divided' if a%11==0 and a%2!=0 else 'Not Divided'
print(numbers(num))