
Year = 2023
Month = 10
Day = 19

def print_date(Year, Month, Day):
    print(f"The date is {Day}/{Month}/{Year}")

print_date(Year, Month, Day)

class Date:
    def __init__(self) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1

today = Date()
today.Year = 2023
today.Month = 10
today.Day = 19

i = 4