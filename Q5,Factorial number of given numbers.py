user=int(input("Please Enter the number : "))
mul=1
for i in range(user,1,-1):
    print(i,"*",end='')
    mul*=i
print(mul)