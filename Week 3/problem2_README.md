# Address Book Management System

## Description:
This project is an Address Book Management System implemented in Python. It allows users to add entries with personal details such as first name, last name, street address, city, state, country, mobile number, and email address. Users can also count occurrences of first names, last names, and street addresses across all entries. The data is persisted to disk using the pickle module, ensuring that the data is retained even after the program is closed.




## Features:

Add Entry: Users can add entries with personal details, ensuring uniqueness of mobile numbers and email addresses.
Count Occurrences: Users can count occurrences of first names, last names, and street addresses across all entries.
Data Persistence: The program stores the address book data in a file using the pickle module, ensuring that the data is retained even after the program is closed.
Error Handling: The program handles errors gracefully, displaying informative messages to the user in case of file not found or other exceptions.
User-Friendly Interface: The program provides a simple command-line interface for users to interact with, prompting them to choose from a list of options.

## How to Use:

Run the program (python address_book.py) in your terminal or command prompt.
Choose one of the following options:
```
1: Add Entry
2: Count Occurrences
3: Save and Exit
```
If you choose to add an entry, enter the required personal details when prompted.
If you choose to count occurrences, the program will display the occurrences of first names, last names, and street addresses across all entries.
If you choose to save and exit, the program will save the address book data to a file (problem2_data_file.pickle) and exit.

## Dependencies:
Python 3.x

## Installation:

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Run the program using the command python address_book.py in your terminal or command prompt.
