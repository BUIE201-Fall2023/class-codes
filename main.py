import sys

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

class Movie:
    def __init__(self, Name, Year, Month, Day) -> None:
        self.Name = Name
        self.ReleaseDate = Date(Year, Month, Day)

class Viewer:
    def __init__(self, Name) -> None:
        self.Name = Name
        self.Movies = []
    
    def add_movie(self, Movie):
        self.Movies.append(Movie)

interstellar = Movie("Interstellar", 2014, 11, 7)
print("interstellar ref count: ", sys.getrefcount(interstellar))

inception = Movie("Inception", 2010, 7, 30)

caner = Viewer("caner")
tamer = Viewer("tamer")

caner.add_movie(interstellar)
print("interstellar ref count: ", sys.getrefcount(interstellar))

caner.add_movie(inception)

tamer.add_movie(inception)

i = 5