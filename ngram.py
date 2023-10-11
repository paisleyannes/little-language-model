'''
name: ngram.py
authors: Paisley Annes
date: 4/11/2023

n-gram language model using my favorite book (Throne of Glass by Sarah J. Maas)

code generates random text using markov chain algorithm based on input text 

'''

import re
import random

def read_file(filename):
    '''This function reads a file and returns the contents'''

    file = open(filename, 'r', encoding="utf8")
    # file = open(filename, 'r')

    contents = file.read()

    file.close()

    return contents


text = read_file('throne1.txt')

# split the text into a list of words
text = text.lower().replace("'", "").replace('.', 'EOS')
text = re.sub('[^A-Za-z]+', ' ', text)
words = text.split()

# create an empty list to store unique words
unique_words = {}

# markov chain will use 2 words to predict the next word
gram = 2

# For each pair of consecutive words, loop checks if  pair is already in the dictionary
for i in range(len(words)- gram):
    key = words[i] + " " + words[i+1]
    
    # If pair is not, a new list with the next word is created. 
    if key not in unique_words:
        unique_words[key] = [words[i + gram]]
    # If pair is already in the dictionary, the program appends the next word to the list
    else:
        unique_words[key].append(words[i + gram])

# random starting point in text 
random_start = random.randint(0, len(words) - gram)
output = " ".join(words[random_start:random_start + gram]) # joins random sequence of 2 words
print("searching with: ", output) # output words initiates loop which generates rest of sentence
next_word = ""

# Selects the last two words of the current output and uses them to look up the list of possible next words in unique_words dictionary
while len(output) < 300:

    last_words = " ".join(output.split(' ')[-gram:])

    if last_words in unique_words:
        next_word = random.choice(unique_words[last_words])
    
    output += " " + next_word

print(output.replace("EOS", "."))
