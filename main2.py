from base2 import *

contacts = AddrBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, TypeError) as e:
            return f"Error: {e}"
    return wrapper

@input_error
def add(item, name, *args):
    if item == "contact":
        name = Name(name)
        record = Record(name)
        record.add_phone(args[0])
        if len(args)>= 2:
            if args[1] != '':
                record.add_email(args[1])
        return contacts.add_contact(record)
    else:
        record = contacts[name]
        item_maps = {
            "phone": record.add_phone,
            "email": record.add_email,
        }
        return item_maps[item](args[0])

@input_error
def change(item, name, *args):
    new_value = args[0]
    old_value = args[1]
    record = contacts[name]
    item_maps = {
        "phone": record.change_phone,
        "email": record.change_email,
    }
    return item_maps[item](old_value, new_value)

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
        return item_maps[item](args[0])


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

def main():

    print("\nAvailable commands: hello, add, get, change, good bye.")
    print("\x1B[4mPlease type command and item for the operation, e.g. add contact\x1B[0m")

    while True:
        user_input = input(">>> ").strip().lower().split()
        try:
            command = user_input[0]
        except:
            print("Enter the command.")
            continue

        if command == "hello":
            print("Welcome to CLI Contacts Book!")
            
        elif command in ["bye", "good bye", "exit", "close"]:
            print("Good Bye!")
            break
    
        elif command == "showall":
            print(showall())

        else:
            try:
                item = user_input[1]
                if item not in ["contact", "phone", "email", "birthday"]:
                    print(f"Can not {command} {item}. Choose between: contact, phone, email or birthday.")
                    continue
            except IndexError:
                print("Invalid command format. Type command and item for the operation.")
                continue
            try:
                action = func_maps[command]
            except KeyError:
                print("Invalid command. Available commands are: hello, add, get, change, good bye.")
            
            if command == "add":
                if item == "contact":
                    name = input("Enter the name: ")
                    if name in contacts:
                        print("Contact already exists.")
                        continue
                    phone = input("Enter the phone: ")
                    email = input("Enter the emails address (optional, press Enter to skip):")
                    print(action(item, name, phone, email))
                    continue
                else:
                    name = input("Enter the name: ")
                    try:
                        contacts[name]
                    except KeyError:
                        print(f"Error: {name} is not in contacts.")
                        continue
                    new_value = input(f"Enter the {item}: ")
                    print(action(item, name, new_value))
            
            elif command == "change" or command == "delete":
                name = input("Enter the name: ")
                try:
                    data = contacts[name].get(item)
                except KeyError:
                    print(f"Error: {name} is not in contacts.")
                    continue
                if len(data)>1:
                    print(f"Which one would you like to {command}?")
                    for i in range(len(data)):
                        print(f"{i+1}: {data[i]}")
                    index = int(input(">>> "))
                    old_value = index - 1
                else: old_value = 0
                if command == "delete":
                    print(action(item, name, old_value))
                    continue
                new_value = input(f"Enter new {item}: ")
                print(action(item, name, new_value, old_value))
            
            elif command == "delete":
                name = input("Enter the name: ")



if __name__ == "__main__":
    main()