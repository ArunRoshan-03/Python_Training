import sys

list_Values =tuple(["As", "B", "C", "D", "A"])
print(list_Values)

l = (1, 343, 5, 342)
print(l)


print(max(list_Values))
print(min(list_Values))
print(len(list_Values))
print(sum(l))


for index in list_Values:
    print(index, end="")

print("\n", list_Values[:1])