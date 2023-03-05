from flask import Flask
import re
import random
import os

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
book_file = os.path.join(base_dir, 'war_and_peace.txt')

with open(book_file, 'r', encoding='utf-8') as file:
    fille = file.read()
words = fille.split()

lst = []
for iword in words:
    word = re.search(r'\b[а-яА-Я]+\b', iword)
    if word:
        lst.append(word.group())
@app.route('/get_random_word')
def get_random_word():
    global lst
    return random.choice(lst)

if __name__ == "__main__":
    app.run(port=55555, debug=True)