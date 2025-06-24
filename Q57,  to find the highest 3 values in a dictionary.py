
user_input = input("Enter dictionary items (key:value key:value ...): ").split(",")

my_dict = {}

for item in user_input:
    key,value = item.split(":")
    my_dict[key] = int(value)
print(my_dict)

values = list(my_dict.values())
values.sort()

print("Top 3 highest values:", values[:3])
