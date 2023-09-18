# ✨ chispas
## Overview
The Language Learning App aims to provide an interactive and adaptive learning experience for individuals looking to improve their language skills. Utilizing OpenAI's ChatGPT for linguistic analysis and tailored educational content, the application offers a multi-faceted approach to language learning.

## Core Features:

- Random Text Blocks: The app will provide the user with a block of text in the language they are trying to learn.
- Word Selection: Users can select or type in words that they find difficult or would like to improve upon.
- Database Storage: These selected "difficult" words are stored in a user-specific database.
- Thematic Analysis: ChatGPT will analyze these words to determine common themes (e.g., past tense verbs, food-related vocabulary).
- Detailed Explanations: The app will provide detailed explanations and examples for each unknown word and its related themes.
- New Examples: Users will then be provided with new example sentences or paragraphs incorporating these "difficult" words.
- Progression: Finally, new text blocks, tailored to each user's progress, will be introduced.

This process will then, theoretically, be applied recursively to progressively teach people a langue in chunks that are related to each other. 


## Setup env

```bash
scripts/setup
```

Run app

```bash
pipenv run python -m main.py
```

Test

```bash
pipenv run tests
```
