"""
Simple Password Generator
"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyleft 2022"
__license__ = "GNU GPLv3"
__version__ = "0.1.0"
__maintainer__ = "VFM | SB"
__status__ = "Development"


from random import choice, shuffle # Built-in Modules
from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits


# GLOBAL Variables
SPECIAL_CHARS = "!@#$%^&*()-_+=[]{};:|,.?~"
ALL_CHARS = ascii_letters + SPECIAL_CHARS + digits
RECOMMENDED = {
    ALL_CHARS: 8,
    ascii_uppercase: 1,
    ascii_lowercase: 1,
    SPECIAL_CHARS: 1,
    digits: 1
}


# Functions
def generate_password(char_set: str, n: int = 1) -> str:
    """
    Generates a Password in Desired Length\n
        Parameters:\n
            char_set\n
            n (Number of Characters)\n
        Returns:\n
            password: str (n number of chars from char_set)
    """
    password = ""
    for i in range(n):
        password += choice(char_set)
    return password

def shuffle_password(password: str) -> str:
    password = list(password)
    shuffle(password)
    return "".join(password)

def remove_excess_chars(password: str, n: int) -> str:
    for i in range(n):
        password.replace(choice(password), "")
    return password

# Main Function
def main():
    print(f"Simple Password Generator -- Version {__version__}")
    operation_command = input("Choose an Operation (suggest | manual)\n").lower()
    password = ""
    if operation_command == "suggest":
        for char_set, n in RECOMMENDED.items():
            password += generate_password(char_set, n)
    elif operation_command == "manual":
        password_length = int(input("Password Length:\n"))
        least_upper = int(input("Minumum Uppercase Letters?\n"))
        password += generate_password(ascii_uppercase, least_upper)
        least_lower = int(input("Minumum Lowercase Letters?\n"))
        password += generate_password(ascii_lowercase, least_lower)
        least_symbols = int(input("Minumum Special Characters?\n"))
        password += generate_password(SPECIAL_CHARS, least_symbols)
        least_digits = int(input("Minumum Digit Characters?\n"))
        password += generate_password(digits, least_digits)
        # calculate total of minimum character sets
        total_chars = least_upper + least_upper + least_symbols + least_digits
        # add remaining to password
        if password_length > total_chars:
            password += generate_password(ALL_CHARS, password_length - total_chars)
        # remove excess from password
        elif total_chars > password_length:
            password = remove_excess_chars(password, total_chars - password_length)
    else:
        print("Invalid Operation Command")
        try_again = input("Do You Want To Try Again? (yes | no)\n").lower()
        if try_again == "yes":
            print()
            main()
        else:
            return
    print(shuffle_password(password))


# Execution
main()
