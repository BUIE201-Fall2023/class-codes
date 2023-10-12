import time

# function parameters are local variables
# global variables can be defined but not a good idea
def my_function(name):
    global age
    age = 15

    print(f"Hello {name} I am my_function")
    print(f"Good to know that you are {age} years old")

age = 12
print(f"Value of age before function fall {age}")
my_function("caner")
print(f"Value of age after function fall {age}")
