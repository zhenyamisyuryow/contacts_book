from collections import UserDict
from datetime import datetime

class AddrBook(UserDict):
    
    def add_contact(self, record):
        key = record.name.value
        value = record
        self[key] = value
    


class Field:
    def __init__(self, value:str):
        self.value = value

    def __repr__(self):
        return f"{self.value}"
        

class Name(Field):
    pass


class Email(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass

class Record(UserDict):

    def __init__(self, name:Name):
        self.name = name
        self.phones = []
        self.emails = []
        self.data = {
            "name": self.name,
            "phone": self.phones,
            "email": self.emails,
        }

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def add_email(self, email):
        self.emails.append(Email(email))

    def change_phone(self, old, new):
        self.phones[old] = Phone(new)

    def change_email(self, old, new):
        self.phones[old] = Email(new)

    def delete_phone(self, phone):
        del self.phones[phone]

    def delete_email(self, email):
        del self.emails[email]

    def __repr__(self):
        return f"{self.data}"