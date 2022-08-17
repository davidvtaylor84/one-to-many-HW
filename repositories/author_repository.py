from db.run_sql import run_sql

from models.author import Author
from models.book import Book


def save(author):
    sql = "INSERT INTO authors(first_name, last_name, country_of_origin) VALUES (%s, %s, %s) RETURNING *"
    values = [author.first_name, author.last_name, author.country_of_origin]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['country_of_origin'] )
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'],result['last_name'], result['country_of_origin'])
    return author


def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)