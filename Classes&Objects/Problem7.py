# 7. Multiple Objects

# Create a class Book with:

# Attributes: title, author, price

# Method display()

# Create a list of book objects and display details of each book.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print("Book title "+ self.title)
        print("Book author " + self.author)
        print("Book price " + str(self.price ))
        
b1 = Book("Python Snake", "Cristopher", 10000)
b2 = Book("Jaguar Story", "Rim",4000)

list_of_books = [b1, b2]

for i in list_of_books:
    i.display()

