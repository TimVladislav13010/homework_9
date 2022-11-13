import sys


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, *kwargs)
            return result
        except TypeError:
            print(f"")
    return wrapper


def handler(commands):

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
    print("hello")


def add():
    print("add")


def change():
    print("change")


def phone():
    print("phone")


def show_all():
    print("show_all")


def good_bye():
    print("good_bye")


def main():
    while True:
        handler_massage = handler(sys.argv[1])
        if handler_massage == good_bye:
            print(f"Good Bye!")
            break
        elif handler_massage == hello or add or change or phone or show_all:
            try:
                handler_massage()
            except TypeError:
                print(f"Такої команди немає. "
                      f"Введіть валідний аргумент (hello, add, change, phone, show_all, good_bye, close, exit, .)")
            break


if __name__ == "__main__":
    main()
