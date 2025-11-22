class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("No of Pages:", self.no_of_pages)


publisher_name = input("Enter Publisher Name: ")
book_title = input("Enter Book Title: ")
book_author = input("Enter Author Name: ")
book_price = float(input("Enter Price: "))
pages = int(input("Enter no of pages: "))

p = Python(publisher_name, book_title, book_author, book_price, pages)

print("\n----- Python Book Details -----")
p.display()