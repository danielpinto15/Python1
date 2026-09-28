class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def show_books(self):
        for book in self.books:
            book["book"].get_info()
            print(f"Quantidade: {book["quantity"]}")

    def add_book(self, book, quantity):
        self.books.append({
           "book": book, 
           "quantity": quantity
        })

    def add_user(self, user):
        self.users.append(user)

    def borrow(self, userBook, user):
        if any(book["book"] == userBook for book in self.books):           
            for book in self.books:
                if book["book"] == userBook:
                    if book["quantity"] > 0:
                        user.add_book(book["book"])
                        book["quantity"] -= 1
                        print(f"Livro emprestado ao {user.name}")
                    else:
                        print(f"O livro não está disponível, {user.name}")
        else:
            print("Esse livro não existe")

    def return_book(self, userBook, user):
        if userBook not in user.books:    
           print("Não tens esse livro para devolver!")
        else:
             for book in self.books:
                if book['book'] == userBook:
                    user.delete_book(userBook)
                    book["quantity"] += 1
                    print("Livro Devolvido com sucesso")