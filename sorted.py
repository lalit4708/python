cars = [
    {'model1':'Yamaha','price':8400,'since':1995},
    {'model1':'Suzuki','price':50000,'since':2019},
    {'model1':'Venus','price':35000,'since':1962},
    {'model1':'Maruti','price':450000,'since':2014}
]

print(sorted(cars, key= lambda d:d['since']))