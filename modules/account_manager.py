import json
from utils.file_handler import read_json_file
from utils.password_utils import hash_password

class AccountManager:
    # This class is responsible for managing user accounts
    def __init__(self):
        self.users_file = 'data/users.json'
        self.users = read_json_file(self.users_file) or {}

    def create_account(self):
        # Create a new user account
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        hashed_password = hash_password(password)   # Hashing the password

        # Storing the hashed password
        new_user = {"username": username, "password": hashed_password}

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
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Load the user data (assuming you have a method or process for this)
        users = self.load_users()  # Placeholder for your user loading logic
        if username in users:
            stored_hash = users[username]['password']
            if verify_password(password, stored_hash):
                print("Login successful.")
                self.current_user = username
                # You might want to set other flags or data indicating a successful login
            else:
                print("Invalid username or password.")
        else:
            print("Username does not exist.")

    def is_user_logged_in(self):
        # Check if a user is currently logged in
        return self.current_user is not None

    def get_current_user(self):
        # Get the username of the currently logged-in user
        return self.current_user

    def logout(self):
        # Log out the current user
        if self.current_user:
            print(f"{self.current_user} has been logged out.")
            self.current_user = None
        else:
            print("No user is currently logged in.")
