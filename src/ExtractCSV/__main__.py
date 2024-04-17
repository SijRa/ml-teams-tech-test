from data_loader import DataLoader


loader = DataLoader()

calls = loader.extract_json_from_file('data/calls.json')
operators = loader.extract_json_from_file('data/operators.json')

print(calls[0])
print(operators[0])