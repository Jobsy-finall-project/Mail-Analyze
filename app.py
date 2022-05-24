from flasgger import Swagger
from flask import Flask, jsonify, request

from Analyze import analyze
from text_extractor import extract_text

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/", methods=["GET"])
def hello_world():
    """Test
        ---
        parameters:
          - name: name
            in: body
            type: string
            required: true
          - name: file
            in: body
            type: base64 string
            required: true
        responses:
          200:
            description: A list of tags for the CV
            schema:
              type: array
              items:
                type: string
                examples:
                  ['Ruby', 'Ruby on Rails', 'Rails']
    """
    result = analyze("ruby on rails")
    return f"<h1>Hello, World!</h1><p>{result}</p>"


@app.route("/", methods=["POST"])
def analyze_request():
    """Analyze a new CV
        ---
        parameters:
          - name: body
            in: body
            type: object
            required: true
            schema:
              properties:
                name:
                  type: string
                file:
                  type: string
        responses:
          200:
            description: A list of tags for the CV
            schema:
              type: array
              items:
                type: string
                examples:
                  ['Ruby', 'Ruby on Rails', 'Rails']
        """
    request_data = request.get_json()
    # print(request_data)
    mail_text = extract_text(data=request_data["file"], file_name=request_data["name"])
    print(mail_text)
    result = analyze(mail_text)
    print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
