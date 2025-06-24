user=input("Please Enter The Sentence meanimum 3 word :")

if len(user)<3:
    print(user,"Plese Enter The Maximum 3 word")
elif user.endswith("ing"):
    print(user + "ly")
else:
    print(user+"ing")


