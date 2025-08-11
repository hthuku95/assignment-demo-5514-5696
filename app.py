from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/")
def home():
    return jsonify({"message": "Flask REST API Demo"})

if __name__ == "__main__":
    app.run(debug=True)