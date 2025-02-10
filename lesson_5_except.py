# age = input("Введите возраст")
# try:
#     if age < 21:
#         print("Не разрешено")
# except TypeError as error:
#     print("Ошибка")
#     print(error)
# except TypeError as type_err:
#     print("Невернйы тип знаечения")
#
import os.path
from idlelib.iomenu import encoding
from zoneinfo import reset_tzpath

# def get_card_price(sku):
#     pass
#
# def get_sale_price(sku):
#     pass
#
#
# def get_product_info(sku):
#     try:
#         card_price = get_card_price()
#     except Exception as err:
#         card_price = 0
#     try:
#         sale_price = get_sale_price()
#     except Exception as err:
#         sale_price = 0
#
#     info = {
#         "card_price": card_price,
#         "sale_price": sale_price
#     }
#     return info

# file = open("myfile.txt", "r", encoding="utf-8")
# text = file.read()
# file.close()
# print(text)


# try:
#     with open("myfile2.txt", "r", encoding="utf-8") as file:
#         text = file.read()
# except FileNotFoundError as err:
#     print(f"Ошибка: {err}")
#     text = ""
# print(text)
#
#
# if os.path.isfile("myfile.txt"):
#     print("okye")
# else:
#     print("no file")



# with open("myfile.txt", "w", encoding="utf-8") as file:
#     file.write("\n!!!!!")
#
# with open("myfile.txt", "w", encoding="utf-8") as file:
#     text = file.read()
#
# print(text)


def validate_age(age):
    if age < 21:
        raise ValueError("wrong age")
    return age


def get_person_info(info):
    print(info)

# age = int(input("Age"))
# try:
#     age = validate_age(age)
# except ValueError as err:
#     print("Error")
#     age = 0
#
# info = {"name": "Alisa", "age": age}
# get_person_info(info)

while True:
    age = int(input("Age"))
    try:
        age = validate_age(age)
        info = {"name": "Alisa", "age": age}
        get_person_info(info)
        break
    except ValueError as err:
        print(err)
