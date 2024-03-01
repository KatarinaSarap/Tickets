import json
from utils.file_handler import read_json_file
from utils.password_utils import hash_password
from utils.password_utils import verify_password


class AccountManager:
    # This class is responsible for managing user accounts
    def __init__(self):
        self.users_file = 'data/users.json'
        self.users = read_json_file(self.users_file) or {}
        self.current_user = None

    def is_admin_logged_in(self):
        # Implement logic to check if the logged-in user is an admin
        # This is a placeholder; adjust according to your authentication logic
        return self.current_user_role == 'admin'

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
                # Check if the username is available
                if username in users:
                    print("An account with this username already exists.")
                    return
                users[username] = new_user
                file.seek(0)
                json.dump(users, file, indent=4)
            print("Account created successfully.")
        except FileNotFoundError:
            # If the file doesn't exist, create it and add the new user
            with open(self.tickets_file, 'w') as file:
                json.dump({username: new_user}, file, indent=4)
            print("Account created successfully.")

    def login(self):
        # Login an existing user
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        try:
            with open(self.users_file, 'r') as file:
                users = json.load(file)
            if username in users and verify_password(password, users[username]['password']):
                print("Login successful")
                self.current_user = username
                # Example adjustment: Set role for the current session
                self.current_user_role = users[username].get('role', 'regular')  # Default to 'regular' if not specified
                print("You have successfully logged in!")
                return True
            else:
                print("Invalid username or password.")
                return False
        except FileNotFoundError:
            print("Unable to load user data.")
            return False

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
