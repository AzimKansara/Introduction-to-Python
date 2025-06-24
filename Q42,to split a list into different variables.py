user=input("Please Enter The List : ")
lst_number=[(i)for i in user.split(",")]

for index, value in enumerate(lst_number):
    print(f"var{index} = {value}")
