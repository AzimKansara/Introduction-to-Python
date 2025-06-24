user=input("Please Enter The Number : ")
lst_number=((i)for i in user.split(","))
unique_lst_number=[]

for i in lst_number:
    if i not in unique_lst_number:
        unique_lst_number.append(i)
    
print("unique lst number :",unique_lst_number)
        

