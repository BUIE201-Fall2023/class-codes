import time 

def check_duplicate_a(check):
    for i in range(len(check) - 1):
        for j in range(i+1, len(check)):
            if check[i] == check[j]:
                return check[i]
    return None

def check_duplicate_b(check):
    already_seen = set()
    for value in check:
        if value in already_seen:
            return value
        else:
            already_seen.add(value)
    return None

check = [1, -2, 4, 7, -2, 5]
result_a = check_duplicate_a(check)

check2 = [1, -2, 4, 7, -3, 5]
result2_a = check_duplicate_a(check2)

check = [1, -2, 4, 7, -2, 5]
result_b = check_duplicate_b(check)

check2 = [1, -2, 4, 7, -3, 5]
result2_b = check_duplicate_b(check2)

check = list(range(50000))
start_b = time.time()
result_b = check_duplicate_b(check)
print ("check_duplicate_b time:", time.time() - start_b)

start_a = time.time()
result_a = check_duplicate_a(check)
print ("check_duplicate_a time:", time.time() - start_a)
