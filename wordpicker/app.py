from flask import Flask, render_template
import random

app = Flask(__name__)

def pick_word():
    words = [
        "elephant", "guitar", "banana", "tree", "house", "butterfly",
        "computer", "pizza", "bicycle", "beach", "penguin", "dragon"
    ]
    return random.choice(words)

@app.route('/')
def index():
    random_word = pick_word()
    return render_template('index.html', random_word=random_word)

if __name__ == '__main__':
    app.run(debug=True)
