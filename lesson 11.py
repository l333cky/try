
# def is_auto_sign(sign):
#     pattern = r'^[A, B, E, K, M, H, O, P, C, T, Y, X]{1}\d{3}[A, B, E, K, M, H, O, P, C, T, Y, X]{2}\d{2,3}$'
#     if __name__ == "__main__":
#         user_input = input("Введите номер")
#         if isinstance(signs, str):
#             if len(sign) == 8 or len(signs) == 9:
#             else:
#                 raise ValueError("Неверный формат ")
#         else:
#             raise ValueError("Неверный формат)

import re


def is_auto_sign(sign: str) -> str:
    pattern = r'^[АВЕКМНОРСТУ]{1}\d{3}[АВЕКМНОРСТУ]{2}\d{2,3}$'

    if isinstance(sign, str):
        if len(sign) == 8 or len(sign) == 9:
            if re.match(pattern, sign):
                return "Спасибо"
            else:
                raise ValueError("Неверный формат")
        else:
            raise ValueError("Неверный формат")
    else:
        raise ValueError("Неверный формат")


if __name__ == "__main__":
    user_input = input("Введите номер: ")
    try:
        result = is_auto_sign(user_input)
        print(result)
    except ValueError as err:
        print(err)