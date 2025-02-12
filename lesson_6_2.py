import json
from idlelib.iomenu import encoding


def validate_age(age: str) -> int:
    if age.isdigit():
        if 0 < int(age) > 150:
            return int(age)
        else:
            raise ValueError("Возраст должен быть от 1 до 150")
    else:
        raise TypeError("Возраст должен быть числом от 1 до 150")

def validate_phone(phone) -> str:
    numbers = []
    if isinstance(phone, str):
        if len(phone) == 11 or len(phone) == 15:
            for i in phone:
                if i.isdigit():
                    numbers.append(i)
            if len(numbers) == 11:
                return phone
            else:
                raise ValueError("Неверный формат телефона")
        else:
            raise ValueError("Неверный формат телефона")
    else:
        raise ValueError("Неверный формат телефона")

def get__user_info() -> tuple[str,str,str]:
    name = input("Введите имя")
    age = input("Введите возраст")
    phone = input("Введите телефон")

    return name, age, phone

def create_user_info(name: str, age: str, phone: str):
    name = name.capitalize()
    age = validate_age()
    phone = validate_phone()

    info = {
        "name": name,
        "age": age,
        "phone": phone
    }
    return info

def write_user_info(info: dict):
    with open("info.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=2, ensure_ascii=False)



def main():
    user_info = get__user_info()
    user = create_user_info(*user_info)
    write_user_info(user)

if __name__ == "__main__":
    main()
