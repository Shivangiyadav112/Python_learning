#take input from user and append those in list
# x = int(input('Enter a number'))
# lst = []
# for i in range(0,x):
#     y = input('Enter a string to append in list')
#     lst.append(y)
# print(lst) 

x = int(input('Enter a number'))

map_ = {
    'str': [],
    'float': [],
    'int' : []
    }
for i in range(x):
    
    datatyp = input('Enter a datatyp ')
    val = input('Enter a value ')
    if datatyp == 'str':
        map_['str'].append(val)
    elif datatyp == 'float':
        map_['float'].append(float(val))
    elif datatyp == 'int':
        map_['int'].append(int(val))
    else :
        print(' plz Initialize a empty list for {datatyp}',format(datatyp))

   
print(map_)
    