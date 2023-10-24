
class Date:
    def __init__(self, Year, Month, Day) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
        self.set_date(Year, Month, Day)

    def print(self):
        print(f"The date is {self.Day}/{self.Month}/{self.Year}")
    
    def set_date(self, Year, Month, Day):
        if not (Month >= 1 and Month <= 12):
            print("Invalid month")
            return False 
        if not (Day >= 1 and Day <= 31):
            print("Invalid day")
            return False 
        ### Add other validations
        self.Year = Year
        self.Month = Month
        self.Day = Day
        return True

today = Date(2023, 10, 24)
print("today: ", id(today))
today.print()

tomorrow = Date(2023, 10, 25)
print("tomorrow: ", id(tomorrow))
tomorrow.print()

tomorrow = today
print("tomorrow: ", id(tomorrow))
tomorrow.print()

def f(date):
    print(type(date), id(date))
    date.print()
    date.set_date(2025, 10, 24)
    # date = Date(2025, 10, 24)
    print(type(date), id(date))
    date.print()

print("today before f: ", id(today))
today.print()
f(today)
print("today after f: ", id(today))
today.print()

# int objects are immutable
# https://www.guru99.com/mutable-and-immutable-in-python.html
def g(i):
    print(type(i), id(i), i)
    i += 5
    print(type(i), id(i), i)

j = 10
print("before g: ", type(j), id(j), j)
g(j)
print("after g: ", type(j), id(j), j)

my_dictionary = {"IE 201": "Caner Taşkın"}

# dict works with immutable key types
# my_dictionary2 = {["IE", "201"] : "Caner Taşkın"}

# everything is an object in Python
my_float = 3.14
print(type(my_float), id(my_float), my_float)
my_float.is_integer()
my_str = f"the value of my_float is {my_float}"
my_str = "the value of my_float is {}".format(my_float)

