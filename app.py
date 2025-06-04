from flask import Flask, request, render_template, jsonify
from datetime import datetime
import json

# Initialize Flask app
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        return jsonify({"error": "File not found"}), 404i
    #made may changes


if __name__ == '__main__':
    app.run(debug=True)
