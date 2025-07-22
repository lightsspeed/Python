#Scenario: You're writing a script to validate if a user-entered port number is valid (between 1 and 65535).


def valid_port(port: int):
    if 1 <= port <= 65535:
        print("Valid")
    else:
        print("Invalid")

valid_port(335000) 