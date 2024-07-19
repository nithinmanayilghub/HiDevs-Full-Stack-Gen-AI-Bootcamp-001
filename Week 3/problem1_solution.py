import pickle
from datetime import datetime
import re

class PersonalInfo:
    def __init__(self, name, dob, is_secret=False):
        self.name = name
        self.dob = dob
        self.is_secret = is_secret
    
    def __str__(self):
        if self.is_secret:
            return f"{self.name}: secret"
        else:
            return f"{self.name}: {self.dob}"

class PersonalInfoManager:

    def __init__(self,filename):
        self.filename = filename
        self.personal_info_dict = self.load_info()

    def load_info(self):
        try:
            with open(self.filename,"rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

    def save_info(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.personal_info_dict, file)

    @staticmethod
    def validate_name(name):
        pattern = '^(?:[A-Za-z])+\\s+(?:[A-Za-z])+$'
        if re.match(pattern,name):
            return True
        else:
            return False

    @staticmethod
    def validate_date(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def input_with_validation(prompt, validation_func, error_msg):
        for _ in range(3):
            value = input(prompt).strip()
            if validation_func(value):
                return value
            print(error_msg)
        return None

    def get_personal_info(self):
        if self.personal_info_dict:
            for person in self.personal_info_dict.values():
                print(person)
        else:
            print("No Personal Informationa available.")

    def add_personal_info(self):
        name = self.input_with_validation(
            "Please enter the name of the person: ",
            self.validate_name,
            "Invalid Name. Please make sure that the name entered is valid."
        )
        if name is None:
            print("Maximum attempts reached.Returning to main menu.")
            return
    
        dob = self.input_with_validation(
            "Please Enter the Date Of Birth in (YYYY-MM-DD):",
            self.validate_date,
            "Invalid date format.Please Enter the date of Birth in (YYYY-MM-DD) format."
        )
        if dob is None:
            print("Maximum attempts reached.Returning to main menu")
            return
        
        is_secret = input("Is the date of birth a secret?[y/n]: ").strip().lower() == 'y'

        self.personal_info_dict[name.title()] = PersonalInfo(name.title(),dob,is_secret)
        self.save_info()
        print(f"Information for {name.title()} added successfully.")


    def main(self):
        actions = {
            'a':self.add_personal_info,
            'g':self.get_personal_info,
            'q':lambda:exit("Exiting program.")
        }

        while True:
            choice = input("'a':Add Details, \n 'g': Get Personal Details, \n 'q': Quit\n").strip().lower()
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    manager = PersonalInfoManager("problem_1_data_file.pickle")
    manager.main()
