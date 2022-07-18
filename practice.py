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

#check strings
txt = 'I am shivangi'
print('shivangi' in txt)
 
 #modify strings
a = "Hello, World!"
print(a.upper()) # print string uppercase letters and a.lower() will print string lower case letters

#strip() function remove white spaces from the begining and ending 
a = "Hello world "
print(a.strip())

#replace function in string
print(a.replace("H", "J")) # will print jello world
   

#The split() method splits the string into substrings if it finds instances of the separator:
a = "hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print(a.capitalize()) #capitalize first charater in string
print(a.casefold()) #Converts string into lower case
print(a.center(100)) #returns a centered string
print(a.count('h')) #counts the charater in string
print(a.encode())  #Returns an encoded version of the string
print(a.endswith('i')) #Returns true if the string ends with the specified value
print(a.expandtabs(10))
print(a.find('d')) #Searches the string for a specified value and returns the position of where it was found