# integer is immutable
# first part 
num1 = 11
num2 = num1

# print("\nbefore num2 value is updated:")
# print("num1:", num1)
# print("num2:", num2)
# print("num1 points to memory location:", id(num1))
# print("num2 points to memory location:", id(num2))

num2 = 22
num1 = 33

# print("\nafter num2 value is updated:")
# print("num1:", num1)
# print("num2:", num2)
# print("num1 points to memory location:", id(num1))
# print("num2 points to memory location:", id(num2))

# second part
#  mutable object - dictionary
dict1 = {
    "value" : 11
    }
dict2 = dict1

print("\nbefore dict2 value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict1 points to memory location:", id(dict1))
print("dict2 points to memory location:", id(dict2))

dict2["value"] = 22
print("\nafter dict2 value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict1 points to memory location:", id(dict1))
print("dict2 points to memory location:", id(dict2))

dict1["value"] = 33
print("\nafter dict1 value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict1 points to memory location:", id(dict1))
print("dict2 points to memory location:", id(dict2))
