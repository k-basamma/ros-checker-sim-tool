from flask import Flask, render_template, request, jsonify
import os
import sys
# Adding backend to path to import checker
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.checker import run_validation

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    # Trigger Code Checker [cite: 10, 36]
    report = run_validation(path)
    return jsonify(report) [cite: 17]

if __name__ == '__main__':
    app.run(port=5000, debug=True)
