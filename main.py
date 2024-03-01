import sys
from modules.account_manager import AccountManager
from modules.ticket_manager import TicketManager
from utils.input_validator import validate_input


def display_main_menu():
    # Display the main menu
    print("\nWelcome to the Ticket Purchase and Verification System")
    print("1. Create 5an account")
    print("2. Login")
    print("3. Buy a ticket")
    print("4. Check a ticket")
    print("5. Exit")
    return input("Please select an option: ")


def main():
    # Create an instance of the AccountManager and TicketManager classes
    account_manager = AccountManager()
    ticket_manager = TicketManager()

    while True:
        # Display the main menu and get the user's choice
        user_choice = display_main_menu()
        if validate_input(user_choice, range(1, 6)):
            user_choice = int(user_choice)

            if user_choice == 1:
                account_manager.create_account()
            elif user_choice == 2:
                account_manager.login()
            elif user_choice == 3:
                ticket_manager.buy_ticket()
            elif user_choice == 4:
                ticket_manager.check_ticket()
            elif user_choice == 5:
                print("Thank you for using the Ticket Purchase and Verification System. Goodbye!")
                sys.exit()
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
