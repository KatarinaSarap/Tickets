import json
import datetime


class TicketManager:
    # This class will handle the logic for buying and checking tickets
    def __init__(self):
        # The file where tickets will be stored
        self.tickets_file = 'data/tickets.json'

    def buy_ticket(self, user=None):
        if not user:
            # Prompt for a guest identifier
            user = input("Enter a name or pseudonym for ticket verification: ")
            print("Guest ticket purchasing as:", user)
        else:
            print(f"Ticket purchase for user: {user}")

        ticket_type = input("Enter ticket type (Train/Bus/Plane/Ship): ")
        price = input("Enter price: ")
        expiration_date = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        new_ticket = {"user": user, "type": ticket_type, "price": price, "expiration_date": expiration_date}

        try:
            with open(self.tickets_file, 'r+') as file:
                tickets = json.load(file)
                tickets.append(new_ticket)
                file.seek(0)
                json.dump(tickets, file, indent=4)  # Add indent parameter for better formatting
            print("Ticket purchased successfully.")
        except FileNotFoundError:
            with open(self.tickets_file, 'w') as file:
                json.dump([new_ticket], file, indent=4)  # Use indent here as well
            print("Ticket purchased successfully.")

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
