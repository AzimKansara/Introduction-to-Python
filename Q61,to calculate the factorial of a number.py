user=int(input("Please Enter The Number: "))

if user<0:
    print("The Factarial is not valide")
else:
    count=1
    for i in range(user,0,-1):
        print(i,"*",end='')
        count*=i
print(count)

       