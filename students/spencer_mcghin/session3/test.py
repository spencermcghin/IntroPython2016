def user_input():
    print("From the menu, please select from the following options: '\n'"
          "1.) Generate a Thank You Letter '\n'"
          "2.) Generate a Donor Report '\n'"
          "3.) Exit '\n'"
          "You may exit the program at any time by typing 'exit' or return to the main menu by typing 'menu'")
    while True:
        choices = ['1', '2', '3', 'exit', 'menu']
        selection = input("> ")
        if selection in choices:
            print("Thanks")
        else:
            print("Please choose an option from the menu.")


user_input()