# -*- coding: utf-8 -*-
import random
import pyperclip

def createsPassword(length, uses_upper=True, uses_lower=True, uses_numbers=True, uses_sp_chars=True):
    """
    Creates a random password based on user-selected options.

    Arguments:
        length (int): Length of password.
        uses_upper (bool): Include uppercase letters.
        uses_lower (bool): Include lowercase letters.
        uses_numbers (bool): Include numbers.
        uses_sp_chars (bool): Include special characters.

    Returns:
        str: Generated password.
    """
    chars = ""

    flag = 0
    if uses_upper:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        flag+=1
    if uses_lower:
        chars += 'abcdefghijklmnopqrstuvwxyz'
        flag+=1
    if uses_numbers:
        chars += '0123456789'
        flag+=1
    if uses_sp_chars:
        chars += '$#!&@()/-}{'
        flag+=1
    if flag == 1:
        raise ValueError("\nYou must select at least three types of characters.")
    if not chars:
        raise ValueError("\nYou must select at least one type of character.")
    
    # Shuffle the chars for more randomness
    mixed_chars = random.sample(chars, k=len(chars))
    mixed_chars = "".join(mixed_chars)
    
    return ''.join(random.choice(mixed_chars) for _ in range(length))

def gets_int(message, minimum=8):
    
   # Verifies that a value equal to or greater than the minimum (8) has been entered
    while True:
        try:
            value = int(input(message))
            if value < minimum:
                print(f"\nOops!\nPlease enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("You must enter a valid number.")
def gets_option(message):
    #Function that asks for the option
    return input(message).strip().upper() == "Y"

def main():
    #Main of the script
    while True:
        print("\nWelcome to the Password Generator")
        length = gets_int("\nEnter the length of your password, the number must be greater than or equal to 8: ", minimum=8)
        uses_upper = gets_option("\nDo you want to include uppercase letters? (Y/N): ")
        uses_lower = gets_option("\nDo you want to include lowercase letters? (Y/N): ")
        uses_numbers = gets_option("\nDo you want to include numbers? (Y/N): ")
        uses_sp_chars = gets_option("\nDo you want to include special characters? (Y/N): ")

        try:
            password = createsPassword(length, uses_upper, uses_lower, uses_numbers, uses_sp_chars)
            print(f"\nYour new password is: {password}\nIt has been copied to the clipboard\n")
            pyperclip.copy(password)
        except ValueError as e:
            print(e)
            continue

        if not gets_option("\nDo you want to generate a new one? (Y/N): "):
            print("\nGoodbye!\n")
            break

if __name__ == "__main__":
    main()