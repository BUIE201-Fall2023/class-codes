print("Hello, world!")
print("From VS Code - Python")
print("Today is 20231005")

# result = input("How are you today?")
# if result == "Good":
#     print ("Great to hear that you are Good!")
# else:
#     print ("Sorry to hear that you are not Good!")

# This is a comment
"""
    This is a multi-line comment
    That continues across the lines
"""

i = 5 #int
print(type(i))

j = 3.41 #float
print(type(j))

intsum = 1 + 2
if intsum == 3:
    print("Yay, I can do int addition!")
else:
    print("This is an int surprise!")

floatsum = 0.1 + 0.2
if floatsum == 0.3:
    print("Yay, I can do float addition!")
else:
    print("This is a float surprise!")

if abs(floatsum - 0.3) < 0.000001:
    print("Yay, I can do accurate enough float addition!")
else:
    print("This is a big float surprise!")

b = True
print(type(b))
notB = False

# Conversions
f = 3.9536356
print(f)
print(type(f))

intF = int(f)
print(intF)
print(type(intF))

# dynamic types in Python
# variable types can "change"
f = int(f)
print(f)
print(type(f))
