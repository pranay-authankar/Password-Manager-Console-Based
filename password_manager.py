# Function to take 'alphabets' only
def input_alpha(message):

    while True:
        print(message, end="")
        inp = input(" -> ").lower().strip()
        if inp and inp.isalpha():
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

# Function to take 'numbers' only
def input_num(message):

    while True:
        print(message, end="")
        inp = input(" -> ")
        if inp and inp.isdigit():
            inp = int(inp)
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

# Function to take only 'numeric or alphabet'
def input_alphanum(message):
    while True:
        print(message, end="")
        inp = input(" -> ")
        if inp and inp.isalnum():
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

# Function to take any kind of input
def input_all(message):
    while True:
        print(message, end="")
        inp = input(" -> ").lower().strip()
        if inp:
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

#Function to take number within a specific range
def input_specific_num(start, end, message):
    while True:
        print(message, end="")
        inp = input(" -> ").strip()
        if inp and  inp.isdigit():
            inp = int(inp)
            if start <= inp <= end:
                return inp
            else:
                print(f"\nInvalid Input\nTry Again\n[Enter number between {start} - {end}]\n")
        else:
            print(f"\nInvalid Input\nTry Again\n[Enter number between {start} - {end}]\n")

# Function for Yes or No
def yes_no(message):
    while True:
        print(message, end="")
        yn = input(" [y/n] : ").strip().lower()
        if yn and yn in "yn":
            match yn:
                case "y": return True
                case "n": return False
        else:
            print("\nInvalid Input\nTry Entering 'y' or 'n'\n")

password_manager = {}

# User Verification
def user_verification(message):
    password = "12345"  # Password to Open Saved-Password Program

    # Loop to verify the user if they enter wrong password
    while True:
        verify = input_all(f"\n{message}\n\nPassword")
        if verify == password:
            return True                                   # When user entered correct password
        else:
            return False    # When user can't remember the password
                

# To add passwords
def add_pw(pw_dict):
     
     # Loop to Add passwords in a single go
     while True:
        website = input_all("\n[Enter 'stop' to stop adding]\n\nEnter Website name")
        if website not in pw_dict and not website == "stop":        # Checks the conditions
            pw_dict[website] = {}                                   # Creates empty dictionary to store {username:password}
            username = input_alphanum("\nEnter username")
            password = input_all("\nEnter Password")
            pw_dict[website][username] = password                   # Assign Password to the website's username
            print(f"\n{"Password Added".center(30,"-")}")

            proceed = yes_no("\nWant to add more Passwords ?")      # Ask to add more 
            if proceed:
                continue
            else:
                return pw_dict
        elif website == "stop":                                     # entering 'stop' will stop adding further
            return pw_dict
        else:                                                       # If website already exist
            print(f"\n{website} already exists\nIf you want to change password, there is seperate function for that\n")
            return pw_dict

# To View All Passwords
def view_all_password(pw_dict):
    i = 1
    for website in pw_dict:
        for username in pw_dict[website]:
            print(f"{i} -> {website} - {username} - {pw_dict[website][username]}")
            i += 1
    print(f"\n{"[ No Passwords Further ]".center(30,"-")}")

# To search password by website's name
def search_by_website(pw_dict):

    # Loop for seraching many passwords in one go
    while True:
        website = input_all("\nEnter Website")
        if website in pw_dict:                                                      # Checks the existence of website
            print(f"\nWebsite : {website} Found!!\n")
            username = list(pw_dict[website].keys())[0]
            print(f"-> {website} - {username} - {pw_dict[website][username]}")      # Displayes it on screen
            proceed = yes_no("\nWant to search any other wesite's credential ?")    # Asks for more searching
            if proceed:
                continue
            else:
                break
        else:                                                                       # If website do not exist
            print(f"\n{website} not available in saved Credentials\nTry Adding it\n")
            return pw_dict

#To update username
def update_username(pw_dict):

    # View all passwords
    view_all_password(pw_dict)

    i = len(pw_dict)
    username_input = input_specific_num(1, i, "\nEnter number before the desired username")         
    website = list(pw_dict.keys())[username_input-1]                                            
    old_username = list(pw_dict[website].keys())[0]                                            

    # Changing to new username
    new_username = input_alphanum("\nEnter New Username").lower().strip()
    pw_dict[website][new_username] = pw_dict[website][old_username]         # Assigning New username
    del pw_dict[website][old_username]                                      # deleting the old username
    print(f"\n{"Username Updated Successfully".center(30, "-")}")
    return pw_dict

# To Update Password
def update_password(pw_dict):

    # view all passwords
    view_all_password(pw_dict)

    # Selecting the desired website and username 
    website_input = input_num("\nEnter Website")
    website = list(pw_dict.keys())[website_input-1]
    username = list(pw_dict[website].keys())[0]

    # Asking old passsword to change to new password
    attempt = 0

    # Loop to provide 3 chances if old password is wrong
    while attempt < 3:
        print(f"\nYou have {3 - attempt} attempts\n")
        old_password = user_verification("Enter program's password to get access to change saved password")       # User enters program's password
        if old_password:          # verifies if the password is correct
            print("\nProgram unlocked\n")
            new_password = input_all("\nEnter New Password")    # User will enter new password
            pw_dict[website][username] = new_password           # Assigning new password
            print(f"\nNew Password for {website} is updated\n")
            break
        # If Program's password is wrong
        else:                                                       
            if attempt != 2:                                        # While attemps left
                proceed = yes_no("\nWould you like to continue ?")  # Ask if they want to continue
                if proceed:
                    attempt += 1                                    # If yes, then attempt attempted increased 
                    continue
                else:
                    print("\nYou can update your password later, whenever you will remember your old password.")
                    break
            else:                                                   # When user didn't left with any attempt
                print("\nNo more attempts left\nTry Again whenever you remember the old password\n")
                return pw_dict

# To combine updating username / password
def update_credential(pw_dict):

    # Loop for the task they want to do
    while True:
        update = input_specific_num(0, 2, "\nWhat do you want to update\n0. Go Back to menu\n1. Username\n2. Password\n\n")
        match update:
            # Calling Update username Function
            case 1:
                update_username(pw_dict)
                proceed = yes_no("\nWant to update anything else?")
                if proceed:
                    continue
                else:
                    break
            # Calling Update Password Function
            case 2:
                update_password(pw_dict)
                proceed = yes_no("\nWant to update anything else?")
                if proceed:
                    continue
                else:
                    break
            # Stop the task of updating
            case 0:
                break

def delete_credentials(pw_dict):

    # Loop to delete many saved passwords in one go
    while True:
        view_all_password(pw_dict)
        delete_credential = input_specific_num(0, len(pw_dict), "\nEnter website")
        website = list(pw_dict.keys())[delete_credential-1]                         # Storing Website's name

        # Deleting Saved Password
        del pw_dict[website]
        print(f"{website} removed successfully")

        # Preventing the delete function to ask further deleting in one go, if there is no saved passwords left
        if len(pw_dict) != 0:
            proceed = yes_no("\nWant to delete any other item?")
            if proceed:
                continue
            else:
                break
        else:
            break

# Complete program for Saved Password Management
def password_management(pw_dict):

    print("\nWelcome to your Password Manager\n")
    # Loop To validate the user, if they enter wrong password
    while True:

        verify = user_verification("Enter program's password to get access to change saved password")
        if verify == False:
            print("\nUser can't remember the password to open the password manager")
            proceed = yes_no("\nWant to Try again?")
            if proceed:
                continue
            else:
                return
        else:
            print("\nProgram unlocked\n")
            break
    # Loop to perform many tasks in one go
    while True:
        # Checking there is any saved password already exists
        if len(pw_dict) != 0:
            print(f"{"-".center(30,"-")}")
            # List of task to the user
            task = input_specific_num(0, 5, "\nTasks:\n1. Add new Password\n2. View All Passwords\n3. Search by Website Name\n4. Update Password / Username\n5. Delete\n0. Stop the program\n\n")
            
            # Matching user's desired task with appropriate function
            match task:
                case 1: add_pw(pw_dict); continue
                case 2: view_all_password(pw_dict); continue
                case 3: search_by_website(pw_dict); continue
                case 4: update_credential(pw_dict); continue
                case 5: delete_credentials(pw_dict); continue
                case 0: break
        # If there is no saved password exists
        else:
            print("\nThere is no saved passwords till now\n")
            add_pw(pw_dict)         # Directly asks the user to add passwords
            if len(pw_dict) != 0:   # If user adds password
                continue
            else:                   # Still user didn't add anything
                break


password_management(password_manager)
