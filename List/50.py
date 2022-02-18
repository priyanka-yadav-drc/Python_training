my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'])
print(my_list)