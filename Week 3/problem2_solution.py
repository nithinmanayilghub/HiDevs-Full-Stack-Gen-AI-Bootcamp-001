import pickle
from collections import defaultdict, Counter
import re

class AddressBook:
    def __init__(self):
        self.address_book = defaultdict(list)
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.mobile_pattern = r'^\d{10}$'
    
    def get_input(self,prompt,pattern,field_name):
      while True:
        user_input = input(prompt)
        if self.validate_input(user_input,pattern,field_name):
          return user_input

    def validate_input(self,input_str,pattern,field_name):
        if re.match(pattern,input_str):
          return True
        else:
          print(f"Invalid {field_name}. Please Enter a valid {field_name}.")
          return False

    def add_entry(self):
        first_name = self.get_input("Enter first name: ",r'^[a-zA-Z\s]+$',"First Name")
        last_name = self.get_input("Enter Last name: ",r'^[a-zA-Z\s]+$',"Last Name")
        street_address = self.get_input("Enter Street Address: ",r'^[a-zA-Z0-9\s]+$',"Street Address")
        city = self.get_input("Enter City: ",r'^[a-zA-Z\s]+$',"City")
        state = self.get_input("Enter State: ",r'^[a-zA-Z\s]+$',"State")
        country = self.get_input("Enter Country: ",r'^[a-zA-Z\s]+$',"Country")
        mobile = self.get_input("Enter Mobile: ",self.mobile_pattern,"Mobile Number")

        while mobile in [entry[6][0] for entries in self.address_book.values() for entry in entries]:
          print("Mobile Number Already Exists. Please try again.")
          mobile = self.get_input("Enter mobile number: ",self.mobile_pattern,"Phone Number")

        email = self.get_input("Enter Email: ",self.email_pattern,"Email ID")

        while email in[entry[6][1] for entries in self.address_book.values() for entry in entries]:
          print("Email ID Already Exists.Please try again.")
          email = self.get_input("Enter Email: ",self.email_pattern,"Email ID")
        
        entries = [first_name.title(),last_name.title(),street_address.title(),city.title(),state.title(),country.title(),(mobile,email)]
        self.address_book[(mobile,email)].append(entries)

    def count_occurrences(self):
        first_names = Counter(entry[0] for entries in self.address_book.values() for entry in entries)
        last_names = Counter(entry[1].lower() for entries in self.address_book.values() for entry in entries)
        streets = Counter(entry[2] for entries in self.address_book.values() for entry in entries)

        print("First Name Occurrences:")
        for name, count in first_names.most_common():
            print(f"{name}: {count}")

        print("\nLast Name Occurrences:")
        for name, count in last_names.most_common():
            print(f"{name}: {count}")

        print("\nStreet Occurrences:")
        for street, count in streets.most_common():
            print(f"{street}: {count}")

    def save_to_disk(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.address_book, file)
        except Exception as e:
            print(f"Error saving to disk: {e}")

    def load_from_disk(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.address_book = pickle.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty address book.")
        except Exception as e:
            print(f"Error loading from disk: {e}")

def main():
    address_book = AddressBook()
    address_book.load_from_disk('problem2_data_file.pickle')
    attempts = 3
    while attempts > 0:
        choice = input("Enter : \n1 to add entry, \n2 to count occurrences, \n3 to save and exit: ")
        if choice in ['1', '2', '3']:
            # Valid choice processing
            if choice == '1':
                address_book.add_entry()
            elif choice == '2':
                address_book.count_occurrences()
            elif choice == '3':
                address_book.save_to_disk('problem2_data_file.pickle')
                break
        else:
            print("Invalid choice. Please try again.")
            attempts -= 1  # Decrement attempts on invalid choice

        if attempts == 0:
            print("You have reached Maximum number of tries.")
if __name__ == '__main__':
    main()