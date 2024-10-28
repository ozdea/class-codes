class Date:
    def __init__(self, Year = 1970, Month = 1, Day = 1) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
        self.set_date(Year, Month, Day)
    
    def print(self):
        print("The date is {}/{}/{}".format(self.Day, self.Month, self.Year))

    def set_date(self, Year, Month, Day):
        if Month < 1 or Month > 12:
            print("Invalid month")
        elif Day < 1 or Day > 31:
            print("Invalid day")
        # additional validation rules
        else:
            self.Day = Day
            self.Month = Month
            self.Year = Year

class Movie:
    def __init__(self, name, release_year, release_month, release_day) -> None:
        self.name = name
        # self.release_year = release_year
        # self.release_month = release_month
        # self.release_day = release_day
        self.release_date = Date(release_year, release_month, release_day)
        self.viewers = []
    
    def add_viewer(self, viewer):
        self.viewers.append(viewer)

class Viewer:
    def __init__(self, name) -> None:
        self.name = name
        self.movies = []

    def see_movie(self, movie):
        self.movies.append(movie)
        movie.add_viewer(self)
        # this would violate the data encapsulation principle
        # movie.viewers.append(self)



joker = Movie("Joker", 2024, 10, 15)
shrek = Movie("Shrek", 2024, 11, 28)
inside_out = Movie("Inside Out", 2024, 8, 19)

caner = Viewer("caner")
tinaz = Viewer("tinaz")

caner.see_movie(joker)
caner.see_movie(inside_out)
tinaz.see_movie(joker)
tinaz.see_movie(shrek)

i = 4