import time

def fibonacci_iterative(n):
    if n <= 2:
        return 1

    prevprev = 1
    prev = 1
    for i in range(n-2):
        current = prevprev + prev
        prevprev = prev
        prev = current
    return current

fib5 = fibonacci_iterative(5)
print(fib5)

def fibonacci_recursive(n):
    if n <= 2:
        return 1
    fib1 = fibonacci_recursive(n-1)
    fib2 = fibonacci_recursive(n-2)
    return fib1 + fib2

fib5recursive = fibonacci_recursive(5)
print(fib5recursive)


n = 40
start_iterative = time.time()
fibonacci_iterative(n)
print(f"fibonacci_iterative({n}) took {time.time() - start_iterative}")

start_recursive = time.time()
fibonacci_recursive(n)
print(f"fibonacci_recursive({n}) took {time.time() - start_recursive}")
