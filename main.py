
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
    # date.set_date(2025, 10, 24)
    date = Date(2025, 10, 24)
    print(type(date), id(date))
    date.print()

print("today before f: ", id(today))
today.print()
f(today)
print("today after f: ", id(today))
today.print()

