"""
Simple Password Generator
"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyleft 2022"
__license__ = "MIT"
__version__ = "0.2.2"
__maintainer__ = "VFM | SB"
__status__ = "Development"


from random import choice, shuffle # Built-in Modules
from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits


# GLOBAL Variables
SPECIAL_CHARS = "!@#$%^&*()_+=[]{};:|,.?~"
ALL_CHARS = ascii_letters + SPECIAL_CHARS + digits
RECOMMENDED = {
    ALL_CHARS: 8,
    ascii_uppercase: 1,
    ascii_lowercase: 1,
    SPECIAL_CHARS: 1,
    digits: 1
}


# Functions
def generate_password(char_set: str, char_count: int = 1) -> str:
    """Generates a Password in Desired Length"""
    password = ""
    i = 0
    while i < char_count:
        password += choice(char_set)
        i += 1
    return password

def shuffle_password(password: str) -> str:
    """Shuffles Password String"""
    password = list(password)
    shuffle(password)
    return "".join(password)

def remove_excess_chars(password: str, excess_count: int) -> str:
    """Removes Excess Characters From Password"""
    i = 0
    while i < excess_count:
        password = password.replace(choice(password), "", 1)
        i += 1
    return password

def insert_dash(password: str, section_length: int) -> str:
    """Inserts Dash (-) Characters at Desired Spaces"""
    pw_list = list(password)
    i = section_length
    while i < len(pw_list):
        pw_list.insert(i, "-")
        i += section_length + 1
    return "".join(pw_list)


# Main Function
def main():
    print(f"Simple Password Generator -- Version {__version__}")
    operation_commands = input(
        "Choose an Operation (random | manual) & (readable)\n"
    ).lower()
    operation_commands = operation_commands.split(" ")
    password = ""
    if "random" in operation_commands:
        for char_set, char_count in RECOMMENDED.items():
            password += generate_password(char_set, char_count)
    elif "manual" in operation_commands:
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
        # if given password_length is greater than total_chars,
        # add remaining number of characters to password
        if password_length > total_chars:
            password += generate_password(ALL_CHARS, password_length - total_chars)
        # else if total_chars is greater than password length
        # remove excess characters from password
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
    # shuffle password for total randomness
    password = shuffle_password(password)
    # if "readable" keyword is given,
    # determine primes of desired password length,
    # then present them to user as options
    if "readable" in operation_commands:
        available_breakpoints = []
        for i in range(1, len(password) + 1):
            # exclude 1 and length value
            if i == 1 or i == len(password):
                continue
            # if number is prime of length, add it to collection
            if len(password) % i == 0:
                available_breakpoints.append(i)
        # user can only choose one of the available breakpoints
        section_length = int(
            input(
                'Prefered Section Lenght? '
                f'({", ".join(map(str, available_breakpoints))})\n'
            )
        )
        if section_length in available_breakpoints:
            password = insert_dash(password, section_length)
        else:
            print("Invalid Breakpoint Value")
    print("\nGenerated Password:\n", password, sep="")


# Execution
main()
