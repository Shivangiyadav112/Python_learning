x = input("Enter a string")
def sum_ofascii(strr):
    sum = 0
    for i in strr:
        sum = sum + ord(i)
    
    return sum

print(sum_ofascii(x))

#using map
def ascii(str):
    return sum(map(ord, str))

print(ascii(x))

print(map(len ,[['shiv'],['angi']]))

# function which takes to string username and password return
#  a string which contain first 4 character of name and last 4 character of password
def fun(username , passw):
    return (username[:5]+passw[len(passw)-4::1])

use = input("Enter user name")
pas = input("Enter password")
print(fun(use,pas))




x = input("Enter a string")
def alpha(strr):
    countt = 0
    for i in range(0,len(strr)-1):
        if ord(strr[i])+1 == ord(strr[i+1]):
            countt+=1
    return countt

print(alpha(x))

