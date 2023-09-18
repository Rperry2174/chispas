import openai
from utils.initialize_open_ai import initialize_openai
initialize_openai()

def generate_detailed_explanations(unknown_words, themes):
    # Create a prompt for ChatGPT that asks for explanations and examples for each unknown word
    learning_language = "spanish"
    known_languge = "english"
    prompt = f"Provide detailed explanations and examples for the following {learning_language} words, considering the following themes of {themes} that I'm not strong at from a linguistic perspective. Give the examples in both {known_languge} and {learning_language} and provide both the current tense as well as the conjugation of those tenses if it is a verb:\n"
    for word in unknown_words:
        prompt += f"- {word}\n"

    # Call ChatGPT to generate the explanations
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=500
    )

    # Extract and return the generated text as the detailed explanations
    explanations = response.choices[0].text.strip()
    
    return explanations
