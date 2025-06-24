user=input("Please Enter the list of Number : ")
lst_number =[int(i) for i in user.split(",")]
lst_new_number = []

for i in lst_number:
    if i not in lst_new_number:
        lst_new_number.append(i)

print("List after removing duplicates:", lst_new_number)
