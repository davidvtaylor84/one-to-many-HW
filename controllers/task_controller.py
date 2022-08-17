from crypt import methods
from urllib import request
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import book_repository
from repositories import author_repository
from models.book import Book

tasks_blueprint = Blueprint("books", __name__)

@tasks_blueprint.route("/books", methods =['GET'])
def books():
    books_list = book_repository.select_all()
    return render_template("books/index.html", all_books = books_list)

@tasks_blueprint.route("/books/<id>", methods = ['GET'])
def get_book(id):
    book_object = book_repository.select(id)
    return render_template("/books/one_book.html", book = book_object)






