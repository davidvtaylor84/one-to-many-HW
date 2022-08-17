from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Thomas", "Pynchon", "USA")
author_repository.save(author1)
author2 = Author("Virginia", "Woolf", "United Kingdom")
author_repository.save(author2)
author3 = Author("Philip K.", "Dick", "USA")
author_repository.save(author3)

book1 = Book("Inherent Vice", author1, "General Fiction", 9783161484100)
book_repository.save(book1)
book2 = Book("To the Lighthouse", author2, "General Fiction", 9783161484786)
book_repository.save(book2)
book3 = Book("Do Androids Dream of Electric Sheep", author3, "Science-Fiction", 9783161484675)
book_repository.save(book3)