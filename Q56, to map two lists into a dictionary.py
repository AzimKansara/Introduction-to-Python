from collections import Counter

keys = ['a', 'b', 'c', 'd']
values = [400, 400, 300, 400]

result = Counter(dict(zip(keys, values)))

print(result)

#without Counter formula:
keys = ['a', 'b', 'c', 'd']
values = [400, 400, 300, 400]

my_dict = dict(zip(keys, values))

print("Mapped Dictionary:", my_dict)

