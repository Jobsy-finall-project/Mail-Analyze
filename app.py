from flask import Flask
from Train import train
from Analyze import analyze

app = Flask(__name__)
train()


@app.route("/")
def hello_world():
    analyze("")
    return "<h1>Hello, World!</h1>"


if __name__ == '__main__':
    app.run()
