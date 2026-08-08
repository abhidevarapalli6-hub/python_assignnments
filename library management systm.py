class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"title": book, "issued": False})
        print(f'"{book}" added to the library.')

    def remove_book(self, book):
        for item in self.books:
            if item["title"].lower() == book.lower():
                if item["issued"]:
                    print("Cannot remove an issued book.")
                else:
                    self.books.remove(item)
                    print(f'"{book}" removed from the library.')
                return

        print("Book not found.")

    def issue_book(self, book):
        for item in self.books:
            if item["title"].lower() == book.lower():
                if item["issued"]:
                    print("Book is already issued.")
                else:
                    item["issued"] = True
                    print(f'"{book}" issued successfully.')
                return

        print("Book not found.")

    def return_book(self, book):
        for item in self.books:
            if item["title"].lower() == book.lower():
                if item["issued"]:
                    item["issued"] = False
                    print(f'"{book}" returned successfully.')
                else:
                    print("This book was not issued.")
                return

        print("Book not found.")

    def display_books(self):
        print("\nLibrary Books")
        print("-" * 40)

        for item in self.books:
            status = "Issued" if item["issued"] else "Available"
            print(f'{item["title"]:<25} {status}')


# Example
library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.issue_book("Python Programming")
library.return_book("Python Programming")
library.remove_book("Machine Learning")

library.display_books()
