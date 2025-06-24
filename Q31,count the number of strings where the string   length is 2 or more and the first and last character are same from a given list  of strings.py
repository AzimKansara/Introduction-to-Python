data = input("Enter strings separated by comma: ")  # abc,xyz,aba,1221,aa,a,mom
strings =data.split(",")
count = 0
for word in strings:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("Count:", count)
