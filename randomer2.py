import random, time

def passwordGeneratorNumbers():
    while True:
        choseRange = str(input("How many digits do you want? Choose between 6-10: "))
        if choseRange == "6":
            passwordss = random.randrange(111111,999999)
        elif choseRange == "7":
            passwordss = random.randrange(1111111, 9999999)
        elif choseRange == "8":
            passwordss = random.randrange(11111111, 99999999)
        elif choseRange == "9":
            passwordss = random.randrange(111111111, 999999999)
        elif choseRange == "10":
            passwordss = random.randrange(1111111111, 9999999999)
        else:
            print("Invalid Access. Try Again")
            time.sleep(1.5)
            continue

        final_passwordss = str(passwordss)
        return final_passwordss

def passwordGeneratorAlphabet(final_passwordss):
    # how many digits is user want ?
    # according to input, upgrade your software
    alphabet = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z")

    uppercase_alphabet = (
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z")

    character = random.choice(alphabet)
    final_passwordss += character
    character = random.choice(uppercase_alphabet)
    final_passwordss = character + final_passwordss
    return final_passwordss

def passwordGeneratorSymbols(final_passwordss):
    symbols = ("!","£","$","½","&","?","*","-","_","+",":",";",",")
    addSymbols = random.choice(symbols)
    final_passwordss += addSymbols
    return final_passwordss

def show(final_passwordss):
        print("All is ready. Please wait for progress.")
        time.sleep(1.0)
        print(final_passwordss)


def final_generator():
    print("Hello.Welcome to the random password generator.")
    print("There are three ways to create a new password:")
    print("1. Only Numbers")
    print("2. With alphabet digits")
    print("3. With symbol digits")
    print("4. Includes numbers with symbols and alphabet digits.")

    choice = input("Please make a choice based on your wish. (1, 2, 3, 4)")
    if choice == "1":
        # final_password is using here!
        final_password = passwordGeneratorNumbers()
        show(final_password)
    # Add other options here

    elif choice == "2":
        final_password = passwordGeneratorNumbers()
        final_password = passwordGeneratorAlphabet(final_password)
        show(final_password)

    elif choice == "3":
        final_password = passwordGeneratorNumbers()
        final_password = passwordGeneratorSymbols(final_password)
        show(final_password)

    elif choice == "4":
        final_password = passwordGeneratorNumbers()
        final_password = passwordGeneratorAlphabet(final_password)
        final_password = passwordGeneratorSymbols(final_password)
        show(final_password)

    else:
        print("Invalid access. Try again.")

    question = input("Do you want to create another password? Type yes or no").upper()
    if question == "YES":
        print("System is rebooting.")
        time.sleep(1.0)
        final_generator()
    else:
        print("Progress is done.")

final_generator()
