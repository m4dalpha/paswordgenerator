import secrets #import secrets library
import string #import string library

def password_generator(password_length): # function which takes 1 argument
        pw_letters = string.ascii_letters # assign all the letters to the variables
        pw_digits = string.digits # assign all digits to the variable
        pw_chars = string.punctuation # assign all characters to the variable
        password_list = [] # empty list
        for i in range(password_length): # loop in the range given by the user input
            password = secrets.choice(pw_letters + pw_digits + pw_chars) # using secrets library to extract one letter, one digit and one char and assign it to the variable
            password_list.append(password) # the result of password will be assigned to the empty list

        final_pass = "".join(password_list) # from the list convert all the chars to a long string

        return final_pass

def user_input_check(): # check if the user has entered a string, negative number or characters
    while True: # this loop will run until the user will input a positive number
        user_input = input("Enter the length of the password: ") # ask the user to input
        if user_input.isdigit() and int(user_input) > 0: # check if the user input is number and higher then 0
            number = int(user_input) # convert the user input into int
            password_generator(number) # call the pas password_generator function
            break # stop the loop
        else: # returns the input if the user has entered a wrong input
            print("Invalid input. Please enter a positive integer greater than zero.")
