'''
name: ngram.py
authors: Paisley Annes
date: 4/11/2023

n-gram language model which simulates a sentence from the input txt file 

code generates random text using markov chain algorithm based on randomly selected first 2 words

'''

import re
import random


def read_file(filename):
    '''This function reads a file and returns the contents'''
    try:
        with open(filename, 'r', encoding="utf8") as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def process_text(text):
    '''This function processes the text and returns a list of words'''
    # Convert to lowercase, replace characters, and split into words
    text = text.lower().replace("'", "").replace('.', 'EOS')
    text = re.sub('[^A-Za-z]+', ' ', text)
    return text.split()

def generate_random_text(words, max_output, gram=3):  # Increased n-gram order to 3
    unique_words = {}

    # Build the Markov chain dictionary
    for i in range(len(words) - gram):
        key = " ".join(words[i:i + gram])
        if key not in unique_words:
            unique_words[key] = [words[i + gram]]
        else:
            unique_words[key].append(words[i + gram])

    # Select a random starting point
    random_start = random.randint(0, len(words) - gram)
    output = " ".join(words[random_start:random_start + gram])
    print("searching with:", output)

    next_word = ""

    # Generate random text using the Markov chain
    while len(output) < max_output:
        last_words = " ".join(output.split(' ')[-gram:])
        if last_words in unique_words:
            # Use a probabilistic approach based on word frequencies
            next_word = random.choice(unique_words[last_words])
        # Check if the next word is 'EOS' and handle accordingly
            if next_word == 'EOS':
                break  # Stop generating if 'EOS' is encountered
        else:
            break  # Stop generating if the last n-gram is not in the dictionary
        output += " " + next_word

    print(output.replace("EOS", "."))

def main(filename, max_output):
    text = read_file(filename)

    if text:
        words = process_text(text)
        generate_random_text(words, max_output)

if __name__ == "__main__":
    main("throne1.txt", 300)
