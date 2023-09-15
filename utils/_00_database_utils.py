import sqlite3

def initialize_database():
    # Connect to SQLite database (it will create a file if it doesn't exist)
    conn = sqlite3.connect('language_learning_app.db')
    
    # Create a cursor object to execute SQL queries
    c = conn.cursor()

    # Create table for users
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    native_language TEXT NOT NULL
                );''')

    # Create table for unknown words
    c.execute('''CREATE TABLE IF NOT EXISTS unknown_words (
                    word_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    word TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(user_id)
                );''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# # Initialize the database by running the function
# initialize_database()


def store_unknown_words(user_id, unknown_words):
    # Connect to SQLite database
    conn = sqlite3.connect('language_learning_app.db')
    
    # Create a cursor object to execute SQL queries
    c = conn.cursor()

    # Store the unknown words in the database
    for word in unknown_words:
        c.execute("INSERT INTO unknown_words (user_id, word) VALUES (?, ?)", (user_id, word))

    # Commit the changes and close the connection
    conn.commit()
