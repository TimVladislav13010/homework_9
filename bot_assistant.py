PHONE_BOOK = {}


"""
Бот помічник.
Працює з командами (hello, add, change, phone, show_all, good_bye, close, exit, .)
"""


def input_error(func):
    """
    Обробник помилок
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return f"Wrong comand."
        except KeyError:
            return f"KeyError"
        except IndexError:
            return f"Wrong index"
        except ValueError:
            return f"ValueError"
    return wrapper


@input_error
def handler(commands):
    return USER_COMMANDS.get(commands, break_f)


def change_input(user_input):
    """
    Функція для обробки введених даних від користувача
    """
    new_input = user_input.split(" ")
    return new_input
    
    
def hello():
    return "How can I help you?"


@input_error
def add(name, number):
    """
    Функція для додавання нового номеру в телефонну книгу
    """
    if name in PHONE_BOOK:
        return f"Цей контакт {name} вже використовується введіть інше ім`я"
    
    phone_number = (name, number)
    PHONE_BOOK.update([phone_number])
    return f"Запис ({name} : {number}) додано до словника"


@input_error
def change(name, number):
    """
    Функціця для змінни існуючого номеру в телефонній книзі
    """
    if name not in PHONE_BOOK:
        return f"{name} імя не знайдено в словнику"
    
    elif not number.isdigit():
        return f"{number} не числово будь ласка введіть числа"
    
    PHONE_BOOK[name] = number
    
    return f"Запис ({name} : {number}) замінено в словнику"


def phone(name):
    """
    Функція повертає номер телефону з телефонної книги
    """
    if not PHONE_BOOK.get(name):
        return f"{name} не знайдено в телефонній книзі"
    phones = PHONE_BOOK.get(name)
    return f"{name} : {phones}"


def show_all():
    """
    Функція для відображення всієї телефонної книги
    """
    show_number = ""
    for key, val in PHONE_BOOK.items():
        show_number += "Ім'я: " + key + ", номер: " + val + "\n"
    return show_number


def good_bye():
    return "Good Bye!"


def break_f():
    """
    Коли користувач введе щось інше крім команд повертається строка про неправильний ввід команди.
    """
    return f"Wrong enter... "


USER_COMMANDS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show_all": show_all,
    "good_bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
    ".": good_bye
}


def main():
    """
    Логіка роботи бота помічника
    """
    while True:
        result = None
        user_input = input("Введіть будь ласка команду "
                                        "(hello, add, change, phone, show_all, good_bye, close, exit, .)")
        changes_commands = change_input(user_input)
        result = handler(changes_commands[0])
        
        if result == good_bye:
            print(result())
            break
        
        elif len(changes_commands) == 1 or result == show_all or result == hello:
            result = handler(changes_commands[0])()
            print(result)
            
        elif len(changes_commands) == 2:
            result = handler(changes_commands[0])(changes_commands[1])
            print(result)
            
        elif len(changes_commands) == 3:
            result = handler(changes_commands[0])(changes_commands[1], changes_commands[2])
            print(result)

        elif len(changes_commands) > 3:
            result = f"({user_input}) - ви ввели невірну команду"
            print(result)
        
        continue


if __name__ == "__main__":
    main()
