import random
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # for test purposes only

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', random=random.random())

if __name__ == '__main__':
    app.run(debug=True)