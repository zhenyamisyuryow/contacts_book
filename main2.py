from base2 import *

contacts = AddrBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

@input_error
def add(item, name, value, *args):
    record = contacts[name]
    item_maps = {
        "phone": record.add_phone,
        "email": record.add_email,
    }
    item_maps[item](value)

@input_error
def change(item, name, new_value, old_value):
    record = contacts[name]
    item_maps = {
        "phone": record.change_phone,
        "email": record.change_email,
    }
    if old_value is None:
        old_value = 0
    item_maps[item](old_value, new_value)

@input_error
def get(item, name, *args):
    return f"{contacts[name][item]}"

@input_error
def delete(item, name, *args):
    if item == "contact":
        del contacts[name]
    else:
        record = contacts[name]
        item_maps = {
            "phone": record.delete_phone,
            "email": record.delete_email,
        }
        item_maps[item](args[1])

@input_error
def showall():
    return contacts.data if len(contacts.data) > 0 else "Contacts book is empty"

func_maps = {
    "add": add,
    "change": change,
    "delete": delete,
    "get": get,
    "showall": showall,
}

@input_error
def main():

    while True:
        print("\nAvailable commands: hello, add, get, change, good bye. \n\x1B[4mPlease type command and item for the operation, e.g add contact\x1B[0m\n")
        user_input = input(">>> ")
        if user_input == "showall":
            print(showall())
        elif user_input == "hello":
            print("Welcome to CLI Contacts Book!")
        elif user_input in ["bye", "good bye", "exit", "close"]:
            print("Good Bye!")
            break
        else:
            user_input = user_input.split()
            command = user_input[0]
            item = user_input[1]
            if command in func_maps and item in ["contact","phone", "email", "birthday"]:
                new_value = None
                old_value = None
                name = input("Enter the name: ")
                if command == "add" and item == "contact":
                    name = Name(name)
                    record = Record(name)
                    phone = Phone(input("Enter the phone number: "))
                    record.add_phone(phone)
                    email = input("Enter the email address (optional, press Enter to skip): ")
                    if email:
                        record.add_email(Email(email))
                    contacts.add_contact(record)
                    continue
                if command == "change":
                    data = contacts[name].get(item)
                    if len(data)>1:
                        print("Which one would you like to change?")
                        for i in range(len(data)):
                            print(f"{i+1}: {data[i]}")
                        index = int(input(">>> "))
                        old_value = index - 1
                if command == "delete":
                    if item == "contact":
                        del contacts[name]
                        continue
                    else:
                        data = contacts[name].get(item)
                        if len(data)>1:
                            print("Which one would you like to delete?")
                            for i in range(len(data)):
                                print(f"{i+1}: {data[i]}")
                            index = int(input(">>> "))
                            old_value = index - 1
                        elif len(data)<=1 and item != "phone":
                            old_value = 0
                        else:
                            print("Can not delete the only phone")
                            continue

                if command not in ["get", "delete"]:
                    new_value = input(f"Enter the {item.removesuffix('s')}: ")

                try:
                    print(func_maps[command](item, name, new_value, old_value))
                except Exception.args as e:
                    print(e)
            else:
                print("Command is not supported!")

if __name__ == "__main__":
    main()