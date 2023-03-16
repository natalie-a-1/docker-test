from flask import Flask

app = Flask(__name__)


@app.route('/assignment')
def assignment5():
    return "This is for assignment 5 in CS 3203"


@app.route('/about')
def about():
    return "Natalie Hill March 16, 2023"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
