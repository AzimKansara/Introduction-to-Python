list1 = list(map(int, input("Enter first list (comma separated): ").split(",")))
list2 = list(map(int, input("Enter second list (comma separated): ").split(",")))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

if common:
    print("Common elements:", common)
else:
    print("No common elements found.")
