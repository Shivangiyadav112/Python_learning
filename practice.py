x = 10
y = "Shivangi"
print(type(x))
print(type(y))

# python allows to assign multiple variables in one line 
f_name , l_name ,c_name = 'Shivangi' , 'Yadav' ,'Arya'
print(f_name)
print(l_name)
print(c_name)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ['apple','mango','grapes']
a,b,c = fruits
print(a)
print(b)
print(c)

x = "5 "
y = "is "
z = "awesome"
print(x + y + z) #it will prinnt 5 is awesome #as all are strings and the + operator concatenate the strings

# r=5
# print(r + y + z) #it will give an error as + operater will not concatenate int and string


#data types
'''Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType'''
