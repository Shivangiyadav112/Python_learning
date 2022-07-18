#18 july
x = int(input("Enter a number"))
for i in range(x):
    op , num1 , num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if op == 'add':
        print(num1 + num2)
    elif op == 'mul':
        print(num1 * num2)
    elif op =='sub':
        print(num1 - num2)
    elif op == 'div':
        print(num1/num2)
    else:
        print("invalid operator")



