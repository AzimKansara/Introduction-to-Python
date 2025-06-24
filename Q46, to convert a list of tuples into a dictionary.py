user=input("Please Enter The Number(e:g,1:a,2:b,3:c) : ")
lst_number=[(i.split(":"))for i in user.split(",")]
dic_number=dict(lst_number)
print(dic_number)