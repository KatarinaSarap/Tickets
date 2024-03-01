import json
import datetime
from modules.account_manager import AccountManager


class TicketManager:
    # This class will handle the logic for buying and checking tickets
    def __init__(self):
        # The file where tickets will be stored
        self.tickets_file = 'data/tickets.json'

    def main(self):
        account_manager = AccountManager()
        ticket_manager = TicketManager()

        while True:
            if account_manager.is_admin_logged_in():
                # Admin specific options
                print("\nAdmin Menu:")
                print("1. Create Tickets")
                print("2. Exit")
                choice = input("Please select an option: ")
                if choice == '1':
                    ticket_manager.buy_ticket()  # Assuming this method now creates tickets
                elif choice == '2':
                    break  # Exit the application
            else:
                # Menu for regular users and guests
                print("\nMenu:")
                print("1. View Available Tickets")
                print("2. Buy a Ticket")
                print("3. Exit")
                choice = input("Please select an option: ")
                if choice == '1':
                    ticket_manager.list_tickets()

                elif choice == '2':
                    ticket_manager.buy_ticket()  # Invokes the ticket buying process
                elif choice == '3':
                    break  # Exit the application

    def list_tickets(self):
        try:
            with open(self.tickets_file, 'r') as file:
                tickets = json.load(file)
        except FileNotFoundError:
            print("No tickets file found.")
            return

        print("\nAvailable Tickets:")
        for idx, ticket in enumerate(tickets, start=1):
            print(
                f"{idx}. {ticket['type']} from {ticket['departure']} to {ticket['destination']} at {ticket['price']} euros, expires on {ticket['expiration_date']}.")

        # Allow users to select a ticket
        try:
            choice = int(input("Enter the number of the ticket you want to view (or 0 to exit): "))
            if choice == 0:
                return
            selected_ticket = tickets[choice - 1]
            print(
                f"You selected a {selected_ticket['type']} ticket from {selected_ticket['departure']} to {selected_ticket['destination']} at {selected_ticket['price']} euros.")
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")

    def buy_ticket(self, user=None):
        if not user:
            # Prompt for a guest identifier
            user = input("Enter a name or pseudonym for ticket verification: ")
            print("Guest ticket purchasing as:", user)
        else:
            print(f"Ticket purchase for user: {user}")

        ticket_type = input("Enter ticket type (Train/Bus/Plane/Ship): ")
        departure = input("Enter the departure place (city or station):")
        destination = input("Enter the destination (city or station):")
        price = input("Enter price: ")
        expiration_date = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        new_ticket = {"user": user, "type": ticket_type, "price": price, "departure": departure, "destination":destination, "expiration date":expiration_date}

        try:
            with open(self.tickets_file, 'r+') as file:
                tickets = json.load(file)
                tickets.append(new_ticket)
                file.seek(0)
                json.dump(tickets, file, indent=4)  # Add indent parameter for better formatting
            print("Ticket made successfully.")
        except FileNotFoundError:
            with open(self.tickets_file, 'w') as file:
                json.dump([new_ticket], file, indent=4)  # Use indent here as well
            print("Ticket made successfully.")

    def check_ticket(self):
        username = input("Enter your (user)name to check your ticket: ")
        try:
            with open(self.tickets_file, 'r') as file:
                tickets = json.load(file)
                user_tickets = [ticket for ticket in tickets if ticket.get("user") == username]
                if not user_tickets:
                    print("No tickets found for this user.")
                    return

                    # Check if any ticket is valid based on the expiration date
                now = datetime.datetime.now()
                valid_tickets = []
                for ticket in user_tickets:
                    expiration_date = ticket.get("expiration_date")
                    if expiration_date:
                        if datetime.datetime.strptime(expiration_date, '%Y-%m-%d') >= now:
                                valid_tickets.append(ticket)
                    else:
                        print("Some tickets are missing an expiration date.")

                if valid_tickets:
                    print("You have valid ticket(s).")
                    # Optionally, provide details about the valid tickets
                else:
                    print("All your tickets have expired or are invalid due to missing expiration date.")
        except FileNotFoundError:
            print("Tickets file not found.")

    if __name__ == "__main__":
        main()
