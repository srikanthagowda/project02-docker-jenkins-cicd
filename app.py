
from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0")

@app.route("/")
def home():
    return jsonify({
        "application": "Project 02 CI/CD Demo",
        "version": APP_VERSION,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
