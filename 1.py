class PhonebookAssistant:
    current_id = 1

    def __init__(self):
        self.contacts = {}

    @staticmethod
    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Give me name and phone please."
            except KeyError:
                return "Contact not found."
            except IndexError:
                return "Invalid command."
        return inner

    @input_error
    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        return "Contact added."

    @input_error
    def change_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            return "Contact updated."
        else:
            return "Contact not found."

    @input_error
    def show_phone(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "Contact not found."

    @input_error
    def show_all(self):
        if self.contacts:
            all_contacts = "\n".join([f"{name}: {phone_number}" for name, phone_number in self.contacts.items()])
            return f"All contacts:\n{all_contacts}"
        else:
            return "No contacts."

def main():
    assistant = PhonebookAssistant()
    while True:
        command = input("Your command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone_number = command.split(" ", 2)
            print(assistant.add_contact(name, phone_number))
        elif command.startswith("change"):
            _, name, new_phone_number = command.split(" ", 2)
            print(assistant.change_contact(name, new_phone_number))
        elif command.startswith("phone"):
            _, name = command.split(" ", 1)
            print(assistant.show_phone(name))
        elif command == "all":
            print(assistant.show_all())
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()