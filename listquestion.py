 
x = int(input("Enter a number"))
lst =[]
for i in range(x):
    op = input().split()
    if op[0] =='push':
        lst.append(op[1])
        print(lst)
    elif op[0] =='pop':
        lst.remove(op[1])
        print(lst)
    elif op[0] =='stop':
        break
# print(lst)

