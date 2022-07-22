# y = lambda n:[i for i in range(n)]
# print(y(10))

#filter function
def even(n):
    return n%2==0

a = filter(even,[1,2,3,4,56,78,76,77]) # gives the values for which the function is returning true
a = list(a)
print(a)