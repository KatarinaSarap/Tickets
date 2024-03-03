User Manual for Ticket Purchase and Verification System
Functionality list(all possible functionalities
# Introduction

This manual provides guidance on using the Ticket Purchase and Verification System, a software solution designed for managing user accounts and ticket transactions, including purchasing and verifying tickets for various transportation services.

System Requirements

Python 3.x installed on your system.
The bcrypt package for Python (install via pip with pip install bcrypt).

Starting the Application:

Navigate to the project directory in your terminal.
Run the application using Python with the command: python main.py.

Main Menu Options:

Upon starting the application, you are presented with the following options:
1. Create an account
2. Login
3. Buy a ticket
4. Check a ticket
5. Exit
Select an option by entering the corresponding number and pressing Enter.
Account Management

Creating an Account:

Select "1" from the main menu.
Enter a username and password as prompted.
Note: The username "admin" is reserved and cannot be used.

Logging In:

Select "2" from the main menu.
Enter your username and password.
The admin username is Admin and password is Pass1ng
Upon successful login, your role (Admin/User) is displayed.

Logging Out:

To log out, navigate back to the main menu and choose to exit the application or log in with a different account.
Ticket Management

Buying a Ticket (User):

Log in with your user account.
Select "3" from the main menu to access the ticket purchase menu.
Follow prompts to view available tickets and select one to purchase by entering the corresponding number.
Confirmation of your purchase, along with ticket details, will be displayed.

Creating Tickets (Admin):

Log in with an account that has admin privileges.
Select "1" from the admin menu to create tickets.
Enter ticket details as prompted, including type, departure, destination, price, expiration date, and extra infromation (Business class/Economy class).
Upon successful creation, a confirmation message is displayed.

Checking a Ticket:

Select "4" from the main menu.
Enter the ticket details as prompted, including type, departure, destination, and price.
The system will then verify whether the ticket is valid, expired, or not found based on the inputted details and the expiration date.

Exiting the Application:

To exit the application, select "5" from the main menu. A farewell message is displayed, and the program terminates.

Troubleshooting & Support:

File Not Found Errors: Ensure all required data files (users.json, tickets.json) are present in the data directory.

bcrypt Errors: Verify that bcrypt is correctly installed in your Python environment.

Input Errors: Ensure that all inputs match the expected format, especially dates and prices.
