
lst = input().split()
str1=""
for i in range(len(lst)):
    lst[i] = int(lst[i])
    
    str1=str1+chr(lst[i])

for  i in range(len(str1)+1):
    print(str1[0:i])
   