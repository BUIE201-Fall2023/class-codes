
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
