
x = int(input('Enter a number '))

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
       
        if datatyp in map_ :
                map_[datatyp].append(val)
        else:
                map_[datatyp] = []
                map_[datatyp].append(val)

print(map_)
    
  
