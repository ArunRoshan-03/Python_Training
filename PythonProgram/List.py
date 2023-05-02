list_Values = ['As', 'B', 'C', 'D', 'A']
print(list_Values)

# Append
list_Values.append(1)
print(list_Values)

# index to find
print(list_Values.index(1))

# insert
list_Values.insert(2, 'atmecs')
print(list_Values)

list_Values2 = ["S", "j", 2, 2]
list_Values.extend(list_Values2)
print(list_Values)

print(list_Values.count(2))

list_Values.reverse()
print(list_Values)

list_Values.remove(2)
print(list_Values)

print(list_Values.pop(2))

# List Comprehension

list = [value for value in str(list_Values) if "B" in value]

print("The A is included in the ", list, end=" ")
