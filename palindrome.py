#palindrome
x = input("Enter a number")
reverse = x[-1::-1]
if (reverse == x):
    print("palindrome")
else:
    print("not palindrome")    