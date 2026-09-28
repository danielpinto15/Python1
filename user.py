class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def delete_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def show_books(self):
        if len(self.books) == 0:
            print("Não tenho livros!")
        else:
            for book in self.books:
                print(book.title) 