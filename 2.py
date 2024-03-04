class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        try:
            phone = Phone(phone_number)
            self.phones.append(phone)
        except ValueError as e:
            print(e)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        print("Phone number not found.")

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                try:
                    phone.value = Phone(new_phone_number).value
                except ValueError as e:
                    print(e)
                return
        print("Phone number not found.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        print("Phone number not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(phone) for phone in self.phones)}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print("Contact not found.")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Contact not found.")