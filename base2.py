from collections import UserDict
from datetime import datetime

class AddrBook(UserDict):
    
    def add_contact(self, record):
        key = record.name.value
        value = record
        self[key] = value
        return "Success! Contact has been added."
    

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
        if phone in [x.value for x in self.phones]:
            return KeyError("Error: This phone already exists.")
        self.phones.append(Phone(phone))
        return "Success! Phone has been added"
    
    def add_email(self, email):
        if email in [x.value for x in self.emails]:
            return KeyError("Error: This email already exists.")
        self.emails.append(Email(email))
        return "Success! Email has been added"

    def change_phone(self, old, new):
        try:
            self.phones[old] = Phone(new)
            return "Success! Phone has been changed!"
        except KeyError:
            return "Error: No such phone for requested contact."
        except IndexError:
            return "Error: Please choose between given options."

    def change_email(self, old, new):
        try:
            self.emails[old]
            try:
                self.emails[old] = Email(new)
                return "Success! Email has been changed!"
            except KeyError:
                return "Error: No such email for requested contact."
            except IndexError:
                return "Error: Please choose between given options."
        except:
            self.emails.append(new)
            return "New email was added as there was no emails to change."

    def delete_phone(self, phone):
        try:
            if phone != 0:
                del self.phones[phone]
                return "Success! Phone has been deleted!"
            else:
                return "Error: Can not delete the only phone."
        except IndexError:
            return "Error: Please choose between given options."


    def delete_email(self, email):
        try:
            self.emails[email]
            try:
                del self.emails[email]
                return "Success! Email has been deleted!"
            except IndexError:
                return "Error: Please choose between given options."
        except IndexError:
            return "Error: There are no emails."

    def __repr__(self):
        return f"{self.data}"