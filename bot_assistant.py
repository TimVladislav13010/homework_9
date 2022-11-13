PHONE_BOOK = {"name": "number"}


def input_error_index(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print(f"Введіть будь ласка команду (hello, add, change, phone, show_all, good_bye, close, exit, .)")
    return wrapper


def input_error_type(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            print(f"Неправильна команда. Введіть будь ласка команду"
                  f" (hello, add, change, phone, show_all, good_bye, close, exit, .)")
    return wrapper


def input_error_value(func):
    def wrapper():
        try:
            return func()
        except ValueError:
            print(f"Неправильне введення. Введіть Ім'я та номер через пробіл Ім'я +380981234567")
    return wrapper


def handler(commands):
    commands = commands.lower()
    users_commands = {
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
    return users_commands.get(commands)


def hello():
    print("How can I help you?")


@input_error_value
def add():
    phone_number = input("Введіть Ім'я та номер телефону через пробіл: ").split(" ")
    PHONE_BOOK.update([phone_number])
    print(f"Запис ({phone_number[0]} : {phone_number[1]}) додано до словника")


@input_error_value
def change():
    name_number = input("Введіть Ім'я та новий номер телефону через пробіл: ").split(" ")
    if len(name_number) != 2:
        raise ValueError
    PHONE_BOOK[name_number[0]] = name_number[1]
    print(f"Запис ({name_number[0]} : {name_number[1]}) замінено в словнику")


def phone():
    name_phone = input("Введіть Ім'я користувача: ")
    phones = PHONE_BOOK.get(name_phone)
    print(f"{name_phone} : {phones}")


def show_all():
    for key, val in PHONE_BOOK.items():
        print(f"Ім'я: {key}, номер: {val}")


def good_bye():
    pass


@input_error_index
@input_error_type
def main():
    while True:

        handler_massage = handler(input("Введіть будь ласка команду "
                                        "(hello, add, change, phone, show_all, good_bye, close, exit, .)"))

        if handler_massage == good_bye:
            print(f"Good Bye!")
            break

        handler_massage()

        continue


if __name__ == "__main__":
    main()
