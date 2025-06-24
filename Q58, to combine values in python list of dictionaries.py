from collections import Counter

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

result = Counter()

for i in data:
    result[i['item']] += i['amount']

print(result)
