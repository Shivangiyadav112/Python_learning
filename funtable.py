#function for printing the table of a number
def tab(n):
    for i in range(1,11):
        mul = i * n
        print(mul)

x = int(input("Enter a number"))
tab(x)