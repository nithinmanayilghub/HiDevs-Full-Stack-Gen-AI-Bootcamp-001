class PersonalInfo:
    def __init__(self,name,dob,is_secret=False):
        self.name = name
        self.dob = dob
        self.is_secret = is_secret
    
    def __str__(self):
        if self.is_secret:
            return f"{self.name}: secret"
        else:
            return f"{self.name}:{self.dob}"

personal_info_dict = {}

import pickle
# Load personal information from existing file

try:
    with open("problem1_data_file.pickle","rb") as file:
        personal_info_dict = pickle.load(file)
except (FileNotFoundError,EOFError):
    pass

# Function to save personal information to a file
def save_info():
    with open("problem1_data_file.pickle","wb") as file:
        pickle.dump(personal_info_dict,file)

def add_personal_info():
    global personal_info_dict  # Declare that you want to use the global variable
    name = input("Please Enter the name of the person: ").title()
    dob = input("Please Enter the  Date of Birth (YYYY-MM-DD): ")
    is_secret = input("Is the date of birth, a secret?[Y/n]: ").lower() == 'y'
    person = PersonalInfo(name,dob,is_secret)
    personal_info_dict[name] = person
    save_info()

attempts = 0

while attempts < 3:
    try:
        choice = input("'a': Add Personal Details,\n'g': Get Personal Details,\n'q': Quit\n")
        if choice == 'a':
            add_personal_info()
        elif choice == 'g':
            for person in personal_info_dict.values():
                print(person)
        elif choice == 'q':
            break
        else:
            print("Invalid Input.Please try again")
            attempts += 1
    except ValueError:
        print("Invalid Input.Please try again")
        attempts += 1
else:
    print("Maximum Limits reached.Exiting Function")









