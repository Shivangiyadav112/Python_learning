x = int(input("Enter a number"))
for i in range(x):
    op = input()
    op_lst = op.split()
 
    if op_lst[0] == "add":
        total = 0
        for num in op_lst[1:]:
            total = total + int(num)
        print(total)
    elif op_lst[0] == "mul":
        mul = 1
        for m in op_lst[1:]:
            mul = mul * int(m)
        print(mul) 