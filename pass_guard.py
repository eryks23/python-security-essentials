import string
import random
import secrets
from colorama import Fore, Style, init

init(autoreset=True)

def check_password(password):

    if len(password) < 8:
        return False

    required = [

        set(string.ascii_lowercase),
        set(string.ascii_uppercase),
        set(string.digits),
        set(string.punctuation)

    ]
    
    password_set = set(password)

    for group in required:
        if not password_set.intersection(group):
            return False
    return True
    
def generate_password():

    pool = string.ascii_letters + string.digits + string.punctuation
    
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    
    password += [secrets.choice(pool) for _ in range(8)]
    random.shuffle(password)
    
    return ''.join(password)

user_input = input("Enter password to check: ")

if check_password(user_input):
    print(Fore.GREEN + Style.BRIGHT + "Password is correct!")
else:
    print(Fore.RED + Style.BRIGHT + "Password too weak. Generating new one...")
    print(Fore.CYAN + "Your new password: " + Style.BRIGHT + generate_password())