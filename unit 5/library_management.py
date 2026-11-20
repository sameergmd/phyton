class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id} | {self.title} by {self.author} | {status}"

class Library:
    def __init__(self):
        self.books = {}
        self.issued = {}  # book_id -> member name

    def add_book(self, book):
        self.books[book.book_id] = book

    def show_books(self):
        for b in self.books.values():
            print(b)

    def issue_book(self, book_id, member):
        book = self.books.get(book_id)
        if book is None:
            print("Book not found.")
        elif not book.available:
            print("Book already issued.")
        else:
            book.available = False
            self.issued[book_id] = member
            print(f"'{book.title}' issued to {member}.")

    def return_book(self, book_id):
        if book_id in self.issued:
            self.books[book_id].available = True
            member = self.issued.pop(book_id)
            print(f"Book returned by {member}.")
        else:
            print("This book was not issued.")

lib = Library()
lib.add_book(Book(1, "Python Basics", "Mark Lutz"))
lib.add_book(Book(2, "Think Python", "Allen Downey"))
lib.add_book(Book(3, "Automate the Boring Stuff", "Al Sweigart"))

while True:
    print("\n1.Show 2.Issue 3.Return 4.Add Book 5.Exit")
    ch = input("Choice: ")
    if ch == "1":
        lib.show_books()
    elif ch == "2":
        lib.issue_book(int(input("Book id: ")), input("Member name: "))
    elif ch == "3":
        lib.return_book(int(input("Book id: ")))
    elif ch == "4":
        lib.add_book(Book(int(input("Id: ")), input("Title: "), input("Author: ")))
    elif ch == "5":
        break
    else:
        print("Invalid choice.")
