import configparser
from flask import Flask, jsonify

config = configparser.RawConfigParser()
config.read('config.properties')

app = Flask(__name__)

if config.getboolean("features", "feature_1") == True:
	message = "Hello, Sasha!"
else:
	message = "Hello, World!"

@app.route("/")
def hello():
	return message 

@app.route("/health")
def health():
	"""Health check endpoint for Kubernetes liveness and readiness probes"""
	return jsonify({"status": "healthy", "service": "hello-gitops"}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050)
