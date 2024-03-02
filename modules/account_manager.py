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
        # Checks if the logged-in user is "admin"
        return self.get_current_user() == "admin"

    def create_account(self):
        username = input("Enter a username: ").strip()
        if username.lower() == "admin":
            print("This username is reserved and cannot be used.")
            return

        password = input("Enter a password: ")
        hashed_password = hash_password(password)  # Hashing the password

        # Attempt to open the users file and add the new user
        try:
            with open(self.users_file, 'r+') as file:
                users = json.load(file)
                if username in users:
                    print("An account with this username already exists.")
                    return
                else:
                    users[username] = {"password": hashed_password}
                    file.seek(0)
                    json.dump(users, file, indent=4)
                    print("Account created successfully.")
        except FileNotFoundError:
            with open(self.users_file, 'w') as file:
                json.dump({username: {"password": hashed_password}}, file, indent=4)
                print("Account created successfully.")

    def login(self):
        # Login an existing user
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ")

        try:
            with open(self.users_file, 'r') as file:
                users = json.load(file)
            if username in users and verify_password(password, users[username]['password']):
                self.current_user = username
                role = "Admin" if username.lower() == "admin" else "User"
                print(f"Login successful. Welcome, {role}!")
                return True, role  # Return both login status and role
            else:
                print("Invalid username or password.")
                return False, None
        except FileNotFoundError:
            print("Unable to load user data.")
            return False, None

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
