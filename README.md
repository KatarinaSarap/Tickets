# Ticket Purchase and Verification System

## Overview
The Ticket Purchase and Verification System is a comprehensive software solution designed to facilitate the management of user accounts and ticket transactions for various transportation services. It offers a user-friendly interface for purchasing and verifying tickets.

## Features and Functionalities
- **Navigation:**
  - An easy to navigate menu
  - The user is asked for input to find out what action they want to take (create account, log in, purchase a ticket, check a ticket or exit the program)
- **Account Management:**
  - Create user accounts with secure password storage.
  - User login and logout capabilities.
  - Reserved admin role for elevated access and functionalities.

- **Ticket Transactions:**
  - Purchase tickets for transportation services (Train, Bus, Plane, Ship).
  - A ticket can be purchased with or without an account.
  - View available tickets with detailed information (type, departure, destination, price, extra infromation(for exampe economy or business class)).
  - After the purchase the user is sent a message, which includes all the information about the ticket.
  - Verify ticket validity based on type, departure, destination, and price.

- **Admin(only) Features:**
  - Exclusive access to ticket creation tools.
  - The Admin can create new tickets with specified details.

## System Requirements
- Python 3.x
- bcrypt package (Install via pip with `pip install bcrypt`)

## Installation
1. Clone the repository to your local machine.
2. Ensure Python 3.x is installed on your system.
3. Install required Python packages:
4. Navigate to the project directory and run the application:

## Usage
1. **Starting the Application:**
- Run `main.py` to start the application and access the main menu.

2. **Navigating the Main Menu:**
- Use the numeric options to navigate through the application's functionalities.

3. **Account Management:**
- Choose to create an account or login from the main menu. Follow the prompts to complete the desired action.

4. **Purchasing and Verifying Tickets:**
- Users can purchase available tickets and check their validity through the menu options.

5. **Admin Functions:**
- Admin users have additional options to create tickets.

## Logging Out and Exiting the Application
- To exit and log out,  select "5" from the main menu. A farewell message is displayed, and the program terminates.

## Troubleshooting
- bcrypt Errors: Verify that bcrypt is correctly installed in your Python environment.
- Input Errors: Ensure that all inputs match the expected format, especially dates and prices.
