user=input("Please Enter The List(for the enter list use space) : ")
lst_number=[(i) for i in user.split()]

if not lst_number:
    print("The List is Empty")
else:
    print("The List is Not Empty") 