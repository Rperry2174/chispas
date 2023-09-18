import openai
import os

def initialize_openai():
    API_KEY = os.environ.get("OPENAI_API_KEY")
    openai.api_key = API_KEY