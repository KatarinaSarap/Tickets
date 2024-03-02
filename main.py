import sys
from modules.account_manager import AccountManager
from modules.ticket_manager import TicketManager
from utils.input_validator import validate_input


def display_main_menu():
    # Display the main menu
    print("\nWelcome to the Ticket Purchase and Verification System")
    print("1. Create an account")
    print("2. Login")
    print("3. Buy a ticket")
    print("4. Check a ticket")
    print("5. Exit")
    return input("Please select an option: ")


def main():
    # Create an instance of the AccountManager and TicketManager classes
    account_manager = AccountManager()
    ticket_manager = TicketManager()

    # Display the main menu and get the user's choice
    while True:
        # Display the main menu and get the user's choice
        user_choice = display_main_menu()
        if validate_input(user_choice, range(1, 6)):
            user_choice = int(user_choice)

            if user_choice == 1:
                if not account_manager.is_user_logged_in():
                    account_manager.create_account()
            elif user_choice == 2:
                if not account_manager.is_user_logged_in():
                    current_user = account_manager.login()
                    if not current_user:
                        print("Login failed. Please try again or create an account.")
            elif user_choice == 3:
                if account_manager.is_admin_logged_in():
                    ticket_manager.admin_menu()
                elif account_manager.is_user_logged_in():
                    # Regular user flow
                    ticket_manager.user_menu()
                else:
                    # Guest flow
                    print("Continues as a guest...")
                    ticket_manager.user_menu()
            elif user_choice == 4:
                if current_user:
                    ticket_manager.check_ticket()
                else:
                    print("Continues as a guest...")
                    ticket_manager.check_ticket()
            elif user_choice == 5:
                print("Thank you for using the Ticket Purchase and Verification System. Goodbye!")
                sys.exit()
        else:
            print("Please try again.")


if __name__ == "__main__":
    main()