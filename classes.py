"""Module supplying classes for manipulating dictionaries"""
from collections import UserDict, defaultdict
from datetime import datetime
import re

class Field:
    "Parent class"
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """class Name works with the contact name"""
    def __init__(self, name):
        super().__init__(name)
class Phone(Field):
    """class Phone works with the contact phone"""
    def __init__(self, phone):
        number = re.search("[0-9]{10}$", phone)
        if number and len(phone) == 10:
            super().__init__(phone)
        else:
            print("Phone number must consist of 10 digits")

class Birthday(Field):
    """class Birthday works with the contact's date of birth"""
    def __init__(self, value):
        birthday = datetime.strptime(value, '%d.%m.%Y')
        super().__init__(birthday)

class Record:
    """class Record manipulates the contact phone number info"""
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        """function adds contact's phone number to the list"""
        phone = Phone(phone)
        self.phones.append(phone)
    def remove_phone(self, check_phone):
        """function removes contact's phone number to the list"""
        for p in self.phones:
            if p.value == check_phone:
                self.phones.remove(p)
    def edit_phone(self, p, new_phone):
        """function edits contact's phone number in the list"""
        for p in self.phones:
            if p.value == new_phone:
                return "No need to edit"
            else:
                self.phones.append(new_phone)
                self.phones.remove(p)
    def find_phone(self, search_phone):
        """function searched and returns contact's phone number in the list"""
        for p in self.phones:
            if p.value == search_phone:
                return p
    def add_birthday(self, birthday):
        """function adds birthday to the contact"""
        try:
            self.birthday = datetime.strptime(birthday, "%d.%m.%Y")
            return 'Birthday added'
        except ValueError:
            return "Birthday should be in format DD.MM.YYYY"
    def show_birthday(self):
        """function shows contact's birthday"""
        try:
            return self.birthday.strftime('%d.%m.%Y')
        except KeyError:
            return 'Contact not found'
    def __str__(self):
        return f"Contact name: {self.name.value}{', phones: '
            + '; '.join(p.value for p in self.phones) if self.phones else ''}{', birthday: '
            + self.birthday.strftime('%d.%m.%Y') if self.birthday else ''}"
class AddressBook(UserDict):
    """class AddressBook works with the contact records"""
    def add_record(self, record):
        """function adds the record into the dictionary"""
        self.data[record.name.value] = record
    def find(self, name):
        """function searches the record in the dictionary"""
        for name in self.data:
            return self.data.get(name)
    def delete(self, name):
        """function deletes the record from the dictionary"""
        if name in self.data.keys():
            self.data.pop(name)
        else:
            return "Error"
    def find_birthdays(self):
        """function searches and returns contacts' birthdays"""
        for contact in self.data.value():
            if contact.birthday:
                print(contact)
            else:
                continue

    def get_birthdays_per_week(self):
        """Function prints a list of colleagues' birthdays for the following 7 days"""
        today = datetime.today().date()
        list_of_birthday_colleagues = defaultdict(list)
        result = ''
        for name, record in self.items():
            # birthday =  record.birthday.value.date()
            birthday_this_year = record.birthday.replace(year=today.year).date()
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year+1)
            else:
                birthday_this_year = birthday_this_year.replace(year=today.year)
            record.birthday = birthday_this_year
        # sorted_list = sorted(book, key = lambda contact: contact["birthday"])
        for name, record in self.items():
            # name = contact["name"]
            next_birthday = record.birthday
            delta_days = (next_birthday - today).days
            str_next_birthday = str(next_birthday)
            if delta_days < 7:
                formatted = datetime.strptime(str_next_birthday, '%Y-%m-%d')
                day_of_the_week = datetime.strftime(formatted, "%A")
                if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
                    list_of_birthday_colleagues['Monday'].append(name)
                else:
                    list_of_birthday_colleagues[day_of_the_week].append(name)
        for day, name in list_of_birthday_colleagues.items():
            result += f"{day}: {', '.join(name)}\n"
        return result
    def __str__(self):
        result = ''
        for key, value in self.data.items():
            result += f"""Contact name: {key}{', phones: '
            + '; '.join(p.value for p in value.phones) if value.phones else ''}{', birthday: '
            + value.birthday.strftime('%d.%m.%Y') if value.birthday else ''}\n"""
        return result
    