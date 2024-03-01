def validate_input(user_input, valid_range):
    """Validates if the user input is an integer and within the valid range."""
    try:
        choice = int(user_input)
        if choice in valid_range:
            return True
        else:
            print(f"Input must be within the range: {min(valid_range)}-{max(valid_range)}")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False
