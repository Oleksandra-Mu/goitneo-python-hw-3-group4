"""Bot assistant that works with phone contacts"""
from classes import AddressBook, Record

book = AddressBook()
def input_error(func):
    """Error decorator"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_birthday":
                return "Please provide contact name and birthday in format DD.MM.YYYY."
            elif func.__name__ == "delete_contact" or \
                 func.__name__ == "show_phone" or func.__name__ == "show_birthday":
                return "Please provide contact name"
            return "Please provide contact name and phone."
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
    if len(phone) != 10:
        return 'Phone number must consist of 10 digits'
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, book):
    """Function checks if a contact is in contacts and substitutes the phone number"""
    name, old_phone, new_phone = args
    if name in book.keys():
        record = book.find(name)
        old_phone = record.phones[0]
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, book):
    """Function checks if a contact is in contacts and prints user's phone number"""
    name = args[0]
    if name in book:
        record = book.find(name)
        return record.show_phones()
    else:
        raise KeyError

def show_all(book):
    """Function prints all contacts from the dictionary"""
    return book.__str__()

@input_error
def add_birthday(args, book):
    """Function adds birthday for the existing contact and creates a new contact with a birthday"""
    name, birthday = args
    if name in book.keys():
        record = book.find(name)
        return record.add_birthday(birthday)
    else:
        record = Record(name)
        book.add_record(record)
        return record.add_birthday(birthday)
@input_error
def show_birthday(args, book):
    """Function checks if a contact is in contacts and prints contact's birthday"""
    if len (args) == 0:
        raise ValueError
    name = args[0]
    record = book.find(name)
    if record:
        return record.show_birthday()
    else:
        raise KeyError

def week_birthdays(book):
    """
    Function checks contacts' birthdays and 
    prints people to congratulate during the following 7 days
    """
    return book.get_birthdays_per_week()

@input_error
def delete_contact(args, book):
    """Function checks if a contact is in contacts removes it"""
    if len (args) == 0:
        raise ValueError
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    elif record:
        book.delete(name)
        return "Record is deleted."

def main():
    """Function communicates with the user and carries out commands"""
    # book = {}
    book = AddressBook()
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
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(week_birthdays(book))
        else:
            print("Invalid command.")

    print(book)

if __name__ == "__main__":
    main()
