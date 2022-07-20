def greet():
    print("hello world")
    return("hii")

var=greet()
print(var) #the retuen staement of function will be printed here

#function to calculate factorial of a number
def fac(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

x = input("Enter a number")
print(x)