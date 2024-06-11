# {1:1,2:4,3:9,4:16}
# square = {num:num**2 for num in range(1,6)}
# print(square)

# string = 'lalit'
# # for i in string:

# word_count = {char:string.count(char) for char in string}
# print(word_count)

# {1:'odd',2:'even'}
odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,6)}
print(odd_even)