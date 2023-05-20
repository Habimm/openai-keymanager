import dotenv
import flask
import flask_cors
import os
import requests

dotenv.load_dotenv()

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/', methods=['POST'])
def home():
  request_data = flask.request.get_json()
  openai_api_key = os.getenv("OPENAI_API_KEY")
  headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json"
  }
  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=request_data)
  return flask.jsonify(response.json()), response.status_code

if __name__ == '__main__':
  app.run(debug=False)
