# 15 july

tup = (1,2,3,4,'hello world')
print(tup)
type(tup)
st = {4,3,4,4,3,2,1}
print(st)
bt = {4,5,6,1,0}
print(bt)
print(type(st))
print("intersection :")
print(st.intersection(bt))
print("union")
print(st.union(bt))

# dictionaries



map_ = {
    'first_name': 'Shivangi',
    'last_name': 'Yadav',
    'company' : 'Regex'
    }
print(map_['first_name'])
# print(map_['company']) #key error bcz this key is not present in dict
print(map_.get('comapny','Not found')) #company key is not present im dict so the default value not found will be printed

print(map_.keys())
print(map_.pop('company')) #company key will be removed from dict popitem() method removes the last inserted item from the dict 
map_.update({'company' : 'regex'})

newdict = map_.copy()
print('updated dictionay' )
print(map_)
print("copy of map_ dict")
print(newdict)


# loop
from traceback import format_exc


lst = [1,2,3,4,5,6,7,8,9,10]
for i in  lst[2:]:       #printing will start from 3
    print(i)

range
two_table = range(2,21,2)
print(list(two_table))

for i in range(1,10) :
    print(i)

for i in range(len(lst)) :
    print(lst[i])
print( '  ')
for i in range(0,len(lst),2):
    print(lst[i])

print( '  ')

for i in [1,2,3]:
    for j in ['a','b','c']:
        print(i,j)

# while loop
i = 0
while i < 5:
    print(i)
    i+=1




