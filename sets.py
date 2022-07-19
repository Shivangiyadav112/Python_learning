dic = { }
while True:
    
    val = input().split()
    if val[0] == 'stop':
        break

    else:
        
        if val[0] in dic:
            dic[val[0]].add(val[1])
        else:
            dic[val[0]] = set()
            dic[val[0]].add(val[1])
             
print(dic)
