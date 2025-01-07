from flask import Flask, request, jsonify, send_file
import joblib
import os

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Welcome to the Machine Learning Model API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['input']])
    return jsonify({'prediction': prediction.tolist()})

@app.route('/report', methods=['GET'])
def report():
    report_path = 'report.pdf'  # Ensure your report is saved as 'report.pdf' in the same directory
    if os.path.exists(report_path):
        return send_file(report_path, as_attachment=True)
    else:
        return "Report not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
