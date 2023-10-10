import time

# if condition:
#     true statement
# elif:
#     another true statement
# else:
#     false statement

# match starting with Python 3.10

i = "a"

if i == "a":
    pass    # handle case 1
elif i == "b":
    pass # handle case 2
elif i == "c":
    pass # handle case 3
else:
    pass # default case

match i:
    case "a": pass # handle case 1
    case "b": pass # handle case 2
    case "c": pass # handle case 3
    case _: pass # default case 

print ("range(10)")
for i in range(10):
    print(i)

print ("range(10, 15)")
for i in range(10, 15):
    print(i)

print ("range(20, 45, 5)")
for i in range(20, 45, 5):
    print(i)

# continue and break
print ("range(10), continue")
for i in range(10):
    if i == 5:
        continue
    elif i == 7:
        break
    print(i)

i = 0
while i < 10:
    print("I'm in the while statement ", i)
    i += 1

# operators
# mathematical operators
# +, -, *, /, //

float_division = 11 / 9
print(type(float_division), "=", float_division)

int_division = 5 // 2
print(type(int_division), "=", int_division)

mod_result = 5 % 2
print(type(mod_result), "=", mod_result)

power_result = 2 ** 5
print(type(power_result), "=", power_result)

# assignment operators
# =, +=, -=, *=, /=, //=

# equality / inequality checks
# ==, <, <=, >, >=, !=, is

# logical operators
# and, or, not

# in
my_set = {4, 5, 10, 34, 3}
if 6 in my_set:
    print ("found 6 in set")
else:
    print ("not found 6 in set")

my_list = [4, 5, 10, 34, 3]
if 6 in my_list:
    print ("found 6 in list")
else:
    print ("not found 6 in list")

# also works for other collections such as dict
my_dict = {
    "IE 201": "Caner",
    "IE 202": "Tınaz"
    }
if "IE 201" in my_dict:
    print ("found IE 201 in dict")
else:
    print ("not found IE 201 in dict")

# also for strings
if "2" in "IE 201":
    print ("found 2 in IE 201")
else:
    print ("not found 2 in IE 201")

print("started building the_list and the_set")

the_list = []
the_set = set()
for i in range(50000000):
    the_list.append(i)
    the_set.add(i)
# print(the_list)
# print(the_set)

print("finished building the_list and the_set")

search = -5

list_start = time.time()
if search in the_list:
    print ("found in list")
print("list search time = ", time.time() - list_start)

set_start = time.time()
if search in the_set:
    print ("found in set")
print("set search time = ", time.time() - set_start)