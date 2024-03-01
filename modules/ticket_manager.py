import json


class TicketManager:
    # This class will handle the logic for buying and checking tickets
    def __init__(self):
        # The file where tickets will be stored
        self.tickets_file = 'data/tickets.json'

    def buy_ticket(self, user):
        # Example of how you might structure a ticket purchase
        print("Ticket purchase for user:", user)
        ticket_type = input("Enter ticket type (Train/Bus/Plane/Ship): ")
        price = input("Enter price: ")
        # Implement actual ticket creation and storage logic here

        # Example: Add ticket to tickets.json
        new_ticket = {"user": user, "type": ticket_type, "price": price}
        try:
            with open(self.tickets_file, 'r+') as file:
                tickets = json.load(file)
                tickets.append(new_ticket)
                file.seek(0)
                json.dump(tickets, file)
            print("Ticket purchased successfully.")
        except FileNotFoundError:
            with open(self.tickets_file, 'w') as file:
                json.dump([new_ticket], file)
            print("Ticket purchased successfully.")

    def check_ticket(self):
        # Implement the logic to check the validity of a ticket
        print("Checking ticket validity...")
        # This is where you'd implement the actual checking logic
