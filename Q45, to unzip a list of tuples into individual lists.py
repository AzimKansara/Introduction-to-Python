
user = input("Please Enter The List (e.g. 1a,2b,3c): ")

tpl_lst = []

for i in user.split(","):
    num = int(i[0])     
    char = i[-1]           
    tpl_lst.append((num, char))  


lst1, lst2 = zip(*tpl_lst)


print("List 1:",list (lst1))
print("List 2:",list (lst2))



