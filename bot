"""Bot assistant that works with phone contacts"""
from classes import AddressBook, Record

book = AddressBook()
def input_error(func):
    """Error decorator"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."

    return inner

def parse_input(user_input):
    """Function analyzes user input and splits the command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    """Function adds new contacts in the contact dictionary"""
    name, phone = args
    book[name] = phone
    return "Contact added."

@input_error
def change_contact(args, book):
    """Function checks if a contact is in contacts and substitutes the phone number"""
    name, phone = args
    if name in book.keys():
        book[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, book):
    """Function checks if a contact is in contacts and prints user's phone number"""
    name = args[0]
    if name in book:
        return book[name]
    else:
        raise KeyError

def show_all(book):
    """Function prints all contacts from the dictionary"""
    return book

def add_birthday(args, book):
    name, birthday = args
    if name in book.keys():
        return Record.add_birthday(birthday)
    else:
        book[name] = birthday

def show_birthday(book):
    return AddressBook.find_birthdays(book)

def birthdays(book):
    return AddressBook.get_birthdays_per_week(book)

def main():
    """Function communicates with the user and carries out commands"""
    book = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

    print(book)

if __name__ == "__main__":
    main()
