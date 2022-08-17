DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  country_of_origin VARCHAR(255)
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  book_name VARCHAR(255),
  genre VARCHAR(255),
  isbn BIGINT,
  author_id INT NOT NULL REFERENCES authors(id)
);

