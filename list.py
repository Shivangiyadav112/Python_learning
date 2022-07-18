# take input from user and append those in list
x = int(input('Enter a number'))
lst = []
for i in range(0,x):
    y = input('Enter a string to append in list')
    lst.append(y)
print(lst)  