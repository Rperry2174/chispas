def get_difficult_words():
    # Prompt the user to enter the words they find difficult
    user_input = input("Please enter the words you find difficult, separated by spaces: ")

    # Convert the user input into a list of words
    difficult_words = user_input.split()

    return difficult_words
