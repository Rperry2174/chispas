import openai
import os

from utils.initialize_open_ai import initialize_openai
from utils._00_database_utils import initialize_database, store_unknown_words
from utils._01_text_utils import display_random_text_block, display_entire_text
from utils._02_word_selection_utils import get_difficult_words
from utils._03_theme_analysis_utils import analyze_themes_with_chatgpt
from utils._04_explanation_utils import generate_detailed_explanations
from utils._05_example_generation_utils import generate_new_examples, generate_progression_text_block

initialize_openai()
initialize_database()

# To display entire block of text to the user
random_text = display_entire_text("00_input_text.txt")
# random_text = display_entire_text("01_input_text.txt")

# Get the list of difficult words from the user
difficult_words_list = get_difficult_words()

# Hardcoded user_id for demonstration; in a real application, you'll dynamically determine this
user_id = 1

# Store the unknown words in the database
store_unknown_words(user_id, difficult_words_list)

# Analyze the themes in the list of unknown words using ChatGPT
themes = analyze_themes_with_chatgpt(difficult_words_list)
print(f"Common themes found: {themes}")

# Generate detailed explanations for the unknown words
explanations = generate_detailed_explanations(difficult_words_list, themes)
print(f"Detailed explanations:\n{explanations}")

# Generate a new example paragraph incorporating the unknown words
new_example = generate_new_examples(difficult_words_list, themes)
print(f"New example paragraph:\n{new_example}")

# Generate a new text block for the next learning cycle
new_text_block = generate_progression_text_block(difficult_words_list, themes, "beginner")
print(f"New text block for progression:\n{new_text_block}")

# Repeat the process for the next learning cycle
