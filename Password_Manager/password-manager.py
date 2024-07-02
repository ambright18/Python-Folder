from cryptography.fernet import Fernet

#define a function to write a crypotography key and then comment the function out
'''def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
# function that handles viewing encrypted passwords save in the passwords.txt file
def view_password():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


#function to add passwords and save them to a txt file
def add_password():
    name = input("Account Name: ")
    passwrd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(passwrd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add or a view a password? Type (view, add) or type 'quit' to exit the password manager ").lower()

    if mode == "quit":
        break

    if mode == "add":
        add_password()
    elif mode == "view":
        view_password()
    else:
        print("Invalid choice.")
        continue