import time

# function parameters are local variables
# global variables can be defined but not a good idea
def my_function(name, age):
    # global age
    age = 15

    print(f"Hello {name} I am my_function")
    print(f"Good to know that you are {age} years old")

age = 12
print(f"Value of age before function fall {age}")
my_function("caner", age)
print(f"Value of age after function fall {age}")

# optional parameters and default values
def foo(i, j, k = 50):
    print(f"i = {i} j = {j} k = {k}")

foo (10, 15)
foo (10, 15, 40)

# next line gives an error since we don't have all required parameters
# foo (10)
