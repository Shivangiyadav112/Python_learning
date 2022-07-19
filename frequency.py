

#calulate the frequency of letters in a string
x = input('Enter a string')
x= x.lower()
dic = {}
for i in x:
    
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)


