import json
from utils.file_handler import read_json_file

class AccountManager:
    # This class is responsible for managing user accounts
    def __init__(self):
        self.users_file = 'data/users.json'
        self.users = read_json_file(self.users_file) or {}

    def create_account(self):
        # Create a new user account
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        # Here, you would ideally hash the password before storing it.
        new_user = {"username": username, "password": password}

        try:
            # Open the file and load the existing users
            with open(self.users_file, 'r+') as file:
                users = json.load(file)
                if username in users:
                    print("An account with this username already exists.")
                    return
                users[username] = new_user
                file.seek(0)
                json.dump(users, file)
            print("Account created successfully.")
        except FileNotFoundError:
            # If the file doesn't exist, create it and add the new user
            with open(self.users_file, 'w') as file:
                json.dump({username: new_user}, file)
            print("Account created successfully.")

    def login(self):
        # Log in to an existing account
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        try:
            # Open the file and load the existing users
            with open(self.users_file, 'r') as file:
                users = json.load(file)
                if username in users and users[username]["password"] == password:
                    print("Login successful.")
                    self.current_user = username
                else:
                    print("Invalid username or password.")
        except FileNotFoundError:
            # If the file doesn't exist, there are no users yet
            print("No accounts found. Please create an account first.")

    def is_user_logged_in(self):
        # Check if a user is currently logged in
        return self.current_user is not None

    def get_current_user(self):
        # Get the username of the currently logged in user
        return self.current_user

    def logout(self):
        # Log out the current user
        if self.current_user:
            print(f"{self.current_user} has been logged out.")
            self.current_user = None
        else:
            print("No user is currently logged in.")
