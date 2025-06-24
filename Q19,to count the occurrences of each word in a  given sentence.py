# Input from user
sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Create a list of already counted words
counted = []

# Loop to count each word
for word in words:
    if word not in counted:
        count = 0
        for w in words:
            if w == word:
                count += 1
        print(f"'{word}': {count}")
        counted.append(word)

