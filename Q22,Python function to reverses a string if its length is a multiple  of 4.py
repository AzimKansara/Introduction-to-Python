user=input("Please Enter The Word (multiplayer of 4 word) : ")

if len(user) % 4 == 0:
        print( user[::-1])  
else:
    print(user) 
