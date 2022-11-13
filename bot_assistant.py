import sys


def handler(comands):

    users_comands = {
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
    return users_comands.get(comands)


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
        handler_massage = handler(str(sys.argv[1]))
        if handler_massage == good_bye:
            print(f"Good Bye!")
            break
        elif handler_massage == hello or add or change or phone or show_all:
            handler_massage()
            break


if __name__ == "__main__":
    main()
