numbers = list(map(int, input("Enter numbers separated by commas: ").split(",")))

numbers.sort()  

print("Second smallest number is:", numbers[1])
