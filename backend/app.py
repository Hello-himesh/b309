import os  # Add at top

port = int(os.environ.get("PORT", 3000))  # Render uses $PORT


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print(f"User said: {user_message}")
    return jsonify({"reply": "Fake ChatGPT response for now!"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)  # Updated line
