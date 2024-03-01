import json


class TicketManager:
    # This class will handle the logic for buying and checking tickets
    def __init__(self):
        # The file where tickets will be stored
        self.tickets_file = 'data/tickets.json'

    def buy_ticket(self, user=None):
        if user:
            print(f"Ticket purchase for user: {user}")
        else:
            print("Guest ticket purchasing.")

        ticket_type = input("Enter ticket type (Train/Bus/Plane/Ship): ")
        price = input("Enter price: ")

        new_ticket = {"user": user, "type": ticket_type, "price": price} if user else {"type": ticket_type,
                                                                                       "price": price}

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
