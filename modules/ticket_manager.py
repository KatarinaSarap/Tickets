import json
import datetime
import sys
from modules.account_manager import AccountManager


class TicketManager:
    # This class will handle the logic for buying and checking tickets
    def __init__(self):
        # The file where tickets will be stored
        self.tickets_file = 'data/tickets.json'

    def main(self):
        ticket_manager = TicketManager()

    def admin_menu(self):
        # Admin specific options
        print("\nAdmin Menu:")
        print("1. Create Tickets")
        print("2. Exit")
        choice = input("Please select an option: ")
        if choice == '1':
            self.buy_ticket()  # This method now creates tickets
        elif choice == '2':     # Exit the application
            sys.exit()

    def user_menu(self):
        # Menu for regular users and guests
        print("\nMenu:")
        print("1. View Available Tickets")
        print("2. Exit")
        choice = input("Please select an option: ")
        if choice == '1':
            self.list_tickets()
            # first shows the list of tickets, then lets pick one for purchase
        elif choice == '2':
            sys.exit()

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
                f"{idx}. {ticket['info']} {ticket['type']} ticket from {ticket['departure']} to {ticket['destination']} for {ticket['price']} euros, expires on {ticket.get('expiration_date', 'N/A')}.")

        # Allow users to select a ticket
        try:
            choice = int(input("Enter the number of the ticket you want to purchase (or 0 to exit): "))
            if choice == 0:
                return
            selected_ticket = tickets[choice - 1]
            print(
                f"Email: Thank you for purchasing a {selected_ticket['info']} {selected_ticket['type']} ticket from {selected_ticket['departure']} to {selected_ticket['destination']} for {selected_ticket['price']} euros, it expires on {selected_ticket.get('expiration_date', 'N/A')}.")

        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")

    def buy_ticket(self):

        ticket_type = input("Enter ticket type (Train/Bus/Plane/Ship): ")
        departure = input("Enter the departure place (city or station):")
        destination = input("Enter the destination (city or station):")
        price = input("Enter price: ")
        expiration_date = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        info = input("Entre extra details about the ticket(Business or Economy):")
        new_ticket = {"type": ticket_type, "price": price, "departure": departure, "destination": destination, "expiration_date": expiration_date, "info": info}

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
        # Ask for ticket details
        ticket_type = input("Enter ticket type (Train/Bus/Plane/Ship): ")
        departure = input("Enter the departure place (city or station): ")
        destination = input("Enter the destination (city or station): ")
        price = input("Enter price: ")

        try:
            with open(self.tickets_file, 'r') as file:
                tickets = json.load(file)

            # Find matching ticket
            matching_tickets = [ticket for ticket in tickets if
                                ticket['type'] == ticket_type and ticket['departure'] == departure and ticket[
                                    'destination'] == destination and str(ticket['price']) == price]

            if not matching_tickets:
                print("No matching ticket found.")
                return

            # Check if the matching ticket is valid based on the expiration date
            now = datetime.datetime.now().date()
            for ticket in matching_tickets:
                expiration_date = datetime.datetime.strptime(ticket['expiration_date'], '%Y-%m-%d').date()
                if expiration_date >= now:
                    print("Ticket is valid.")
                    return

            # If no valid ticket found
            print("Ticket is invalid or expired.")
        except FileNotFoundError:
            print("Tickets file not found.")

    if __name__ == "__main__":
        main()