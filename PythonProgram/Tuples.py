list_Values = tuple(["As", "B", "C", "D", "A"])
print(list_Values)

list_number = (1, 343, 5, 342)
print(list_number)

print(max(list_Values))
print(min(list_Values))
print(len(list_Values))
print(sum(list_number))

for index in list_Values:
    print(index, end="")

print("\n", list_Values[:1])
