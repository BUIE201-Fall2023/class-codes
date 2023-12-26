l = [30, 4, 34, 13, -6]

l_sorted = sorted(l)

i = 4

# list comprehension
s = ["caner", "tamer", "mustafa", "necati"]

s_uppercase = []
for current in s:
    s_uppercase.append(current.capitalize())

print(s_uppercase)

s_comp = [x.capitalize() for x in s]
print(s_comp)

# set comprehension
s_comp_set = {x.capitalize() for x in s}
print(s_comp_set)

b = [2, 5, 9, 10, 15, 30, 50]

# O(log n) algorithm on an ordered list
# binary_search(b, 8)
