from abc import ABC,abstractmethod

#Abstract class 'Printable' acts as an interface

class Printable(ABC):
    #Abstract method that must beb implamented by any subclass
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable)

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"Book: {self.title} by {self.author}")

#create an instannce of the 'book' class and call the 'print_info' method

book = Book("The Great Gatsby", "F.Scott Fitzgerald")
book.print_info()

