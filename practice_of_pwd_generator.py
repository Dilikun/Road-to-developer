import random
import string


# password generation function
def generate_password(min_length, numbers=True, special_characters=True):
    # generate letters, numbers, special characters from ascii
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # variable that contain all the item that user asked for,  then add them to this
    characters = letters
    # if argument got numbers then it's True and aw should include them to this variable
    if numbers:
        characters += digits
    # It doesn't matter if condition  above works or not in any way this condition will run
    # if argument got special characters
    if special_characters:
        characters += special

    # Create a variable that has criteria for password: number and special characters
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # Main loop that will work until we not meet criteria or length of password is less than minimum length
    while not meets_criteria or len(pwd) < min_length:
        # Create a variable that has criteria for password: number and special characters
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # make value True then check if it needs to be False
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        # It doesn't matter if condition  above works or not in any way this condition will run
        if special_characters:
            # and uses here to check if it really has number criteria and special characters
            meets_criteria = meets_criteria and has_special

    return pwd


# main function
def main():
    min_length = int(input("Enter the minimum length: "))
    # return True only if it has 'y' that's why we use "==" on 'y'
    # lower method uses for change user's input to what we can include to condition
    has_number = input('Do you want to have numbers (y/n)?: ').lower() == 'y'
    has_special = input('Do you want to have special characters (y/n)?: ').lower() == 'y'
    pwd = generate_password(min_length, has_number, has_special)
    print("The generator password is:", pwd)


if __name__ == "__main__":
    main()
