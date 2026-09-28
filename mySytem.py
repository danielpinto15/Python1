from library import Library
from user import User
from book import Book

#3 livros
book_1984 = Book("1984", "George Owell", 1949)
book_clean_code = Book("Clean Code", "Robert Martin", 2008)
book_harry_potter = Book("Harry Potter e a Pedra Filosofal", "JK Rollin", 1997)
book_harry_potter2 = Book("Harry Potter e a Pedra Filosofal2", "JK Rollin", 1997)

#2 users
user_joao = User("João", "joãobatista@god.com")
user_maria = User("Maria", "mariabatista@god.com")

#1 library
library = Library()

#add books
library.add_book(book_1984, 2)
library.add_book(book_clean_code, 1)
library.add_book(book_harry_potter, 1)

#add users
library.add_user(user_joao)
library.add_user(user_maria)

#João pede emprestado 1984
library.borrow(book_1984, user_joao)
#Maria pede o Clean code
library.borrow(book_clean_code, user_maria)
#Maria pede o 1984
library.borrow(book_1984, user_maria)
#mostrar os livros do joão
user_joao.show_books()
#joão devolve o 1984
library.return_book(book_harry_potter2, user_joao)
user_joao.show_books()
#joão tenta devolver novament o 1984
library.return_book(book_1984, user_joao)