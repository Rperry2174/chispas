import random

def display_random_text_block(filename='input_text.txt'):
    # Read the file into a list, each line as a separate element
    with open(filename, 'r', encoding='utf-8') as f:
        text_blocks = f.readlines()

    # Randomly choose one block of text
    random_block = random.choice(text_blocks).strip()

    # Display the randomly chosen block of text to the user
    print(f"Here is a random block of text:\n{random_block}")

    return random_block

def display_entire_text(filename='input_text.txt'):
    # Read the entire file into a string
    with open(filename, 'r', encoding='utf-8') as f:
        entire_text = f.read()

    # Display the entire text to the user
    print(f"Here is the entire text:\n{entire_text}")

    return entire_text
