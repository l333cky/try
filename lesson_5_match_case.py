# from calendar import month
# month = input("Введите месяц: ")
#
# match month:
#     case "1":
#         print("янв")
#     case "2":
#         print("фев")
#     case "3":
#         print("мар")
#     case "4":
#         print("апр")
#     case "5":
#         print("май")
#     case "6":
#         print("июн")
#     case "7":
#         print("июл")
#     case "8":
#         print("авн")
#     case "9":
#         print("сен")
#     case "10":
#         print("окт")
#     case "11":
#         print("ноя")
#     case "12":
#         print("дек")
#     case _:
#         print("wrong"
import sys
from idlelib.iomenu import encoding


def main_menu():
    text = """
    1. Показать книги\n
    2. Добавить книгу\n
    3. Найти книгу\n
"""
    print(text)

def process_menu():
    action = input(">>> ")
    return action

def show_book():
    with open("books.txt", "a+", encoding="utf-8") as file:
        file.seek(0)
        books = file.read()
    if not books:
        print("Книг нет")
    else:
        print(books)

def add_book():
    author = input("Введите автора")
    title = input("Введите название: ")
    year = input("Введите год издания: ")
    book = f"{author} - {title} - {year}"
    return book

def write_book_to_file(book):
    with open("books.txt", "a+", encoding="utf-8") as file:
        file.write(book+"\n")


def search_book():
    print("Поиск книги")

while True:
    main_menu()
    action = process_menu()
    match action:
        case "1":
            show_book()
        case "2":
            book = add_book()
            write_book_to_file(book)
        case "3":
            search_book()
        case "0":
            sys.exit()
        case _:
            print("wrong")