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

def fibonacci_memoized(n, previous_values):
    if n <= 2:
        return 1
    if n in previous_values:
        return previous_values[n]
    fib1 = fibonacci_memoized(n-1, previous_values)
    fib2 = fibonacci_memoized(n-2, previous_values)
    previous_values[n] = fib1 + fib2
    return fib1 + fib2

previous_value = {}
fib5memoized = fibonacci_memoized(5, previous_value)

def fibonacci_tail_rec(n,a=0,b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_tail_rec(n-1, b, a+b)
# seems to be about the same speed or faster than memoized


n = 500
start_iterative = time.time()
fibonacci_iterative(n)
print(f"fibonacci_iterative({n}) took {time.time() - start_iterative}")

#start_recursive = time.time()
#fibonacci_recursive(n)
#print(f"fibonacci_recursive({n}) took {time.time() - start_recursive}")

start_memoized = time.time()
fibonacci_memoized(n, {})
print(f"fibonacci_memoized({n}) took {time.time() - start_memoized}")

start_tail_rec = time.time()
fibonacci_tail_rec(n)
print(f"fibonacci_tail_rec({n}) took {time.time() - start_tail_rec}")