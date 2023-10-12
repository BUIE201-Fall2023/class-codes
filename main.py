import time

def factorial(n):
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

fact5 = factorial(5)
print(f"5! = {fact5} calculated iteratively")

recursive_fact5 = factorial_recursive(5)
print(f"5! = {recursive_fact5} calculated recursively")

# mind the maximum recursion depth 
# recursive_fact1000 = factorial_recursive(1000)
# print(f"1000! = {recursive_fact1000} calculated recursively")

n = 997
start_iterative = time.time()
factorial(n)
print("Iterative time: ", time.time() - start_iterative)

start_recursive = time.time()
factorial_recursive(n)
print("Recursive time: ", time.time() - start_recursive)
