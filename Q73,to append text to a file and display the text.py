file = open("text.txt", "a")
file.write("\nAppended line using another method.")
file.close()

file = open("text.txt", "r")
print(file.read())
file.close()
