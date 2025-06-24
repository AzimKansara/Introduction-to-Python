data = input("Enter numbers separated by space: ")
numbers =list(map(int,data.split(",")))

largest = numbers[0]
smallest = numbers[0]
total = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total += num

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
