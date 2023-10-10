
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

