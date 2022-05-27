from flasgger import Swagger
from flask import Flask, jsonify, request

from repo.tag_repo import add_tag
from src.Analyze import analyze
from src.text_extractor import extract_text

app = Flask(__name__)
swagger = Swagger(app)


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
    mail_text = extract_text(data=request_data["file"], file_name=request_data["name"])
    result = analyze(mail_text)
    return jsonify(result)


@app.route("/tag", methods=["POST"])
def new_tag():
    """Add new Tag to the tag pool
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
        responses:
          200:
            description: OK
            schema:
              type: string
              examples:
                'OK'
    """
    request_data = request.get_json()
    new_tag_to_add = request_data["name"]
    add_tag(new_tag_to_add)
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
