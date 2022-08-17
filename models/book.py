class Book:
    def __init__(self, book_name, author, genre, isbn, id = None):
        self.book_name = book_name
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.id = id