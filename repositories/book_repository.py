from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

def save(book):
    # print(book.author.__dict__)
    sql = "INSERT INTO books(book_name, author_id, genre, isbn) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.book_name, book.author.id, book.genre, book.isbn]
    results = run_sql(sql, values)
    print(results)
    # print("results in repo", results)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['book_name'], author, row['genre'], row['isbn'], row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['book_name'], author, result['genre'], result['isbn'], result ['id'])
    return book


def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)
