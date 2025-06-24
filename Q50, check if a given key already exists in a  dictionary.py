
my_dict = {'x': 100, 'y': 200, 'z': 300}


key = input("Enter the key you want to check: ")


if key in my_dict:
    print(f"Yes, the key '{key}' exists.")
else:
    print(f"No, the key '{key}' does not exist.")
