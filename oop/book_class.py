#Attributes:
#title (str): The title of the book.
#author (str): The author of the book.
#ear (int): The publication year of the book.
#Magic Methods:
#Constructor (__init__): Initializes a Book instance with title, author, and year.
#Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
#String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
#Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
# book_class.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")


    