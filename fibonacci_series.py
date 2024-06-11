# def fibonacci_series():
#     a = 1
#     b = 2
#     series = []
#     for i in range(1,11):
#         c = a + b
#         a = b
#         b = c
#         series.append(c)
#     return series

a = 1
b = 2
for i in range(1,11):
    c = a + b
    a = b
    b = c
    print(c)