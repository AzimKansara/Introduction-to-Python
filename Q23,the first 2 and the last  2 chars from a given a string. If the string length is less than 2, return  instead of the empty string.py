user=input("Please Enter The Word(word is maximm greterthan 2 : ")

if len(user)<2:
    print(" ")
else:
    print(user[:2]+user[-2:])