import string
import getpass 

def check_pwd():
    password =  getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1
    
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    
    if strength == 1:
        remarks = "Very Easily Exploitable"
    elif strength == 2:
         remarks = "Easily Exploitable"
    elif strength == 3:
        remarks = "Somewhat Exploitable"
    elif strength == 4 :
        remarks = "Hard to Exploit"
    elif strength == 5 :
        remarks = "Very Hard to Exploit"

    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} digits")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password strength: {strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False ):
    valid = False
    if another_pwd:
            choice= input('Do you want to enter another password (y/n): ')
    else:
            choice= input('Do you want to check pwd strength (y/n): ')
    while not valid:
            if choice.lower() == "y":
                return True
            elif choice.lower() == "n":
                return False
            else:
                print("Invalid input, try again")
if __name__ == '__main__':
    print('Welcome to the password strength checker')
    as_pwd = ask_pwd()
    if as_pwd:
        while check_pwd:
            check_pwd()
            as_pwd = ask_pwd(True)
        else: print("Exiting program...")
