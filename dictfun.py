file = open('demo.txt','r')
def fun_(file):
    dic ={}
    data = file.readlines()
    # print(data)

    for i in data:
        sub , name = i.split()
       
        if sub in dic:
            dic[sub].add(name)
        else:
            dic[sub] = set()  
            dic[sub].add(name)
    print(dic)

fun_(file)


    


