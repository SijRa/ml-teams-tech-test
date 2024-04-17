from data_loader import DataLoader
from math import floor


loader = DataLoader()

calls = loader.extract_json_from_file('data/calls.json')
operators = loader.extract_json_from_file('data/operators.json')

# print(calls[0])
# print(operators[0])

operatorTable = {}

for index, operator in enumerate(operators):
    operator = operators[index]['attributes']['operator']
    prefix = operators[index]['attributes']['prefix']
    operatorTable[int(prefix)] = operator

ids = []
dates = []
numbers = []
operators = []
riskScores = []

def get_phone_group(phone):
    phone_group = str(phone)[::-1][:8]
    return phone_group[::-1][:4]

print()
# input: 449487659320
print(get_phone_group(449487659320))
# output: 8765

def find_operator(phone_group):
    prefix_group = floor(int(phone_group)/1000)*1000
    try:
        operator = operatorTable[prefix_group]
    except KeyError:
        return 'Unknown'
    return operator

print()
# input: 4438, 5300, 6473
print(find_operator(4438))
print(find_operator(5300))
print(find_operator(6473))
# output: 'O2', 'Three', 'Unknown' 

for call in calls:
    ids.append(call['id'])
    dates.append(call['attributes']['date'].split('T')[0])

    try:
        number = call['attributes']['number'] 
    except KeyError:
        number = 'Withheld'

    numbers.append(number)

    operator = 'Unknown'
    if number != "Withheld":
        group = get_phone_group(int(number[1:]))
        operator = find_operator(group)
    operators.append(operator)
    

    riskScore = call['attributes']['riskScore']
    if call['attributes']['redList'] == True:
        riskScore = 0

    riskScores.append(riskScore)    


print()

print(ids[:6])
print(dates[:6])
print(numbers[:6])
print(operators[:6])
print(riskScores[:6])

print()

print(len(ids), end=',')
print(len(dates), end=',')
print(len(numbers), end=',')
print(len(operators), end=',')
print(len(riskScores), end=',')
