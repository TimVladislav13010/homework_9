import sys


def handler():

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
    print(sys.argv[1])
    return users_comands.get(sys.argv[1])


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
        handler_massage = handler()

        if handler_massage == good_bye:
            break


if __name__ == "__main__":
    main()
