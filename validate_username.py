# You're validating usernames before provisioning cloud access.

#1 username more than 4 characters
#2 username should include numericals atleast one
#3 a dot is a only valid no special characters allowed no spaces allowed.

def validate_username(username: str):

    if len(username) <= 4:
        return False
    

    if not any(char.isdigit() for char in username):
        return False
    
    dot_count = username.count('.')
    if dot_count != 1 or ' ' in username or not username.replace('.', '').isalnum():
        return False
    
    return True

# Test the function
test_usernames = ["user1.123", "usr1.", "user12", "user.name1", "user.name.1", "user name.1", "user@name.1"]
for username in test_usernames:
    print(f"{username}: {validate_username(username)}")