# Approach 1 to create the String variable
Str = str("Arun")
print(Str)

# Approach 2 to create the string variable
name = 'Arun Roshan'
print(name)

# Approach3 we need to print 3 time with out using any looping condition
print(name * 3)

# slicingString
print(name[0:7])
print(name[0:])
print(name[5:7])
print(name[:5])

# Ord() and chr()

print(ord('q'))
print(chr(113))

# String Function
print(
    len(name)
)
print(
    max(name)
)
print(
    min(name)
)

# In and Not In opertor
Name2 = "kutty"
print(Name2 in name)
print(Name2 is not name)
from builtins import print

# Testing String
dummy_data = str("Welcome To Learn Python Program      ")

print(dummy_data.isalnum())
print("Capitalize", dummy_data.capitalize())
print("Case Fold data :", dummy_data.casefold())
print("Ends with ", dummy_data.endswith("am "))
print("It will move and align data :", dummy_data.center(60))
print("it will find the index :", dummy_data.index("e", 6, 10))
print("it will find the index :", dummy_data.index("Learn"))
print("it will find the index :", dummy_data.find("a", 6, 10))
print("it will find the index :", dummy_data.find("Python"))
print("It will expand the Tabs:", dummy_data.expandtabs(30))
print("it will find variable has fully lowercase:", dummy_data.lower().islower())
print("it will find variable has fully lowercase:", dummy_data.upper().isupper())
print("All first text should be captial letter :", dummy_data.istitle())
print("It will find the count of the letter on the variable:", dummy_data.count("P"))
print("Contains:", dummy_data.__contains__("Learn"))
print("right side it will strip:", dummy_data.rstrip())
print("this method will swapcase:", dummy_data.swapcase());
print("It will replaced ", dummy_data.replace("Learn", "Learning"))

# How can you check if a string contains a particular substring in Python?
print("How can you check if a string contains a particular substring in Python?")
first_Word = "  hello, world   "
second_Word = "aba"
if second_Word in first_Word:
    print("First words contain second word")
else:
    print("First words not contain in second word")

# How can you convert a string to all uppercase or all lowercase in Python?
print("How can you convert a string to all uppercase or all lowercase in Python?")

if first_Word.isupper() or first_Word.islower():
    print("Its a upper cases or lower cases")
elif first_Word.isupper() or first_Word.islower() != -1:
    print("The word is not in upper case just now only i changed into upper case : %s" % (first_Word.upper()))
    print("The word is not in upper case just now only i changed into upper case : %s" % (first_Word.lower()))
else:
    print("its not upper case")

# How can you remove whitespace characters (e.g., spaces, tabs, newlines) from the beginning or end of a string in Python?
print(
    "How can you remove whitespace characters (e.g., spaces, tabs, newlines) from the beginning or end of a string in Python?")

if first_Word.isspace() != -1:
    print("We strip the word" + first_Word.strip() + "into like this")
else:
    print("the Word didn't have any spaces or tab ")

# How can you split a string into a list of substrings based on a delimiter in Python?
print("How can you split a string into a list of substrings based on a delimiter in Python?")

print(first_Word.split(", "))

# How can you concatenate two or more strings together in Python?
print("How can you concatenate two or more strings together in Python?")

if second_Word is not first_Word:
    third_Word = first_Word.rstrip() + second_Word
    print("Two string or joined :{} ".format(third_Word))
else:
    print("We can't join this two string")

# How can you replace all occurrences of a substring in a string with a new substring in Python?
print("How can you replace all occurrences of a substring in a string with a new substring in Python?")
print(first_Word.replace("world", "worlds"))

# How can you get the length of a string in Python?
print("How can you get the length of a string in Python?")
print(third_Word.__len__())

# How can you reverse a string in Python?
print("How can you reverse a string in Python?")

print(second_Word[::-1])

# How can you check if a string is a palindrome (i.e., reads the same forwards and backwards) in Python?
print("How can you check if a string is a palindrome (i.e., reads the same forwards and backwards) in Python?")
if second_Word in second_Word[::-1]:
    print("its a palindrome")
else:
    print(" tis not a palindrome")
    print(second_Word[::-1])
