
Year = 2023
Month = 10
Day = 19

def print_date(Year, Month, Day):
    print(f"The date is {Day}/{Month}/{Year}")

print_date(Year, Month, Day)

class Date:
    def __init__(self, Year, Month, Day) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
        self.set_date(Year, Month, Day)

        # class attributes are shared across all objects
        class_attribute = 5   

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

today = Date(2023, 10, -19)
print("today: ", id(today))
# violates data encapsulation / data hiding principles
# today.Year = 2023
# today.Month = 10
# today.Day = 19

today.set_date(2023, 10, -19)
print("today: ", id(today))

today.set_date(2023, 10, 19)
print("today: ", id(today))

today.print()

tomorrow = Date(2023, 10, 20)
print("tomorrow: ", id(tomorrow))
# tomorrow.set_date(2023, 10, 20)
tomorrow.print()

i = 4