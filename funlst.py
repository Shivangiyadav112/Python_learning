


def funlst(lst):

    lst.append("hi")
    lst.append("hello")
    lst.append("he")
    return lst

lst = []
print(funlst(lst))


# functiion to return true if the string is capiital
def strr(st):
    if st == st.upper():
        return True
    else:
        return False

x = input("Enter a string")
print(strr(x))