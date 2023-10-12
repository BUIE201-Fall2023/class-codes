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
# i and j are positional parameters
# k and l are keyword parameters
def foo(i, j, k = 50, l = 100):
    print(f"i = {i} j = {j} k = {k} l = {l}")

foo (10, 15)
foo (10, 15, 40)

# next line gives an error since we don't have all required parameters
# foo (10)

foo (10, 15, l=80)

foo (10, 15, k = 70, l=80)

def sum(i, j, k = 0):
    return i + j + k

result = sum (4, 6)
print(result)

result2 = sum (4, 6, 10)
print(result2)

# arbitrary arguments are treated as a tuple
def sum_all(*inputs):
    total = 0
    for i in inputs:
        total += i
    return total

sum0 = sum_all()
sum1 = sum_all(1)
sum2 = sum_all(4, 5)
sum3 = sum_all(4, 5, 19)
