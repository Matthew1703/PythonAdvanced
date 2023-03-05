from flask import Flask
import random

cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

app = Flask(__name__)

@app.route('/cats')
def catss():
    global cats
    return random.choice(cats)

if __name__ == "__main__":
    app.run(port=5555, debug=True)