from flask import Flask
from flask import request
from Train import train
from Analyze import analyze

app = Flask(__name__)
train()


@app.route("/", methods=["GET"])
def hello_world():
    result = analyze("you")
    return f"<h1>Hello, World!</h1><p>{result}</p>"


@app.route("/", methods=["POST"])
def analyze_request():
    request_data = request.get_json()
    print(request_data)
    result = analyze(request_data["body"])
    res = ""
    if result["accepted_score"] > result["rejected_score"]:
        res = "accepted"
    elif result["accepted_score"] < result["rejected_score"]:
        res = "rejected"
    else:
        res = "cant decide"
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
