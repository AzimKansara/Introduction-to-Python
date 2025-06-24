user = input("Enter a string: ")

letter_count = {}

for i in user:
    if i not in letter_count:
        letter_count[i] = user.count(i)

print(letter_count)
