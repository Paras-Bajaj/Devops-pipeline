# app/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python DevOps Pipeline!"

@app.route("/health")
def health():
    return jsonify(status="OK"), 200

@app.route("/info")
def info():
    return {
        "app": "python-devops-pipeline",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
