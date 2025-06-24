user=input("Please Enter The List : ")
lst_number=[int(i)for i in user.split(",")]
unique_lst=[]

for i in lst_number:
    if i not in unique_lst:
        unique_lst.append(i)
print(unique_lst)

