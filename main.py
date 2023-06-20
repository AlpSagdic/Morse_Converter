from data import morse_alphabet, logo, entrance
from time import sleep

def encryption():
    encrypted_message = ""
    message = input("What's your message: ").upper()

    #To convert each letter to morse code.
    for i in range(len(message)):
        value = morse_alphabet[message[i]]
        encrypted_message += value
    print(f"Your message is:{encrypted_message}")


def decode():
    morse_code = str(input("What's your morse code(Please separate letters with '/'):\n")).split("/")
    crypted_message = ""

    #To conver each letter from morse code to normal letter.
    for i in range(len(morse_code)):
        for key, value in morse_alphabet.items():
            if value == morse_code[i]:
                crypted_message += key
    print(f"Your message is: {crypted_message}")


should_cont = True
while should_cont:
    print(logo)
    print(entrance)
    answer = input("What do you want to do: ").lower()
    if answer == "quit":
        print("Goodbye!")
        should_cont = False

    elif answer == "encryption":
        encryption()
        sleep(2)

    elif answer == "decode":
        decode()
        sleep(2)

    else:
        print("Please enter a valid transaction!")
        should_cont = False
