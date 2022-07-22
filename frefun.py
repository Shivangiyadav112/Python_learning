file = open('random.txt','r')
data = file.read().split()
dict = {}
def frequency(file):
  
    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    file.close()

frequency(file)

file1 = open('random.txt','w')
for key, value in dict.items():
    file1.write(str(key)+ ' '+str(value)+'\n')



