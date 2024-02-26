# Step  1: Book კლასის შექმნა
# კლასის განსაზღვრა,რომელიც წარმოადგენს წიგნებს.
class Book:
    def __init__(self, title, author, publication_year):
        # წიგნის მონაცემების ინიცირება
        self.title = title
        self.author = author
        self.publication_year = publication_year

# Step  2:  `BookManager` კლასის შექმნა
# კლასის განსაზღვრა,რომ წიგნების კოლექციის სამართავად
class BookManager:
    def __init__(self):
        # წიგნების შესანახად ცარიელი სიის ინიცირება
        self.books = []

    def add_book(self, book):
        # წიგნის დამატება წიგნების სიაში
        self.books.append(book)

    def display_books(self):
        # სიაში ყველა წიგნის ჩვენება
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

    def search_book_by_title(self, title):
        # წიგნის მოძებნა სათაურის მიხედვით
        for book in self.books:
            if book.title == title:
                return book
        return None

# Step  3: Console User Interface-ის შექმნა
# ძირითადი ფუნქცია კონსოლის აპლიკაციის გასაშვებად
def main():
    # BookManager ინსტანსის შექმნა
    book_manager = BookManager()

    # უსასრულო ციკლი კონსოლის აპლიკაციის გასაშვებად
    while True:
        # მენიუს პარამეტრების ჩვენება
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")

        # მომხმარებლის არჩევანი მიღება
        choice = int(input("Enter your choice: "))

        # წიგნის დამატება სიაში
        if choice ==  1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter publication year: "))
            book_manager.add_book(Book(title, author, year))

        # ყველა წიგნის ჩვენება
        elif choice ==  2:
            book_manager.display_books()

        # წიგნის სათაურის მიხედვით მოძებნა
        elif choice ==  3:
            title = input("Enter book title to search: ")
            found_book = book_manager.search_book_by_title(title)
            if found_book:
                print(f"Found: {found_book.title} by {found_book.author} ({found_book.publication_year})")
            else:
                print("Book not found.")

        # აპლიკაციიდან გასვლა
        elif choice ==  4:
            break

        # არასწორი არჩევანი
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
