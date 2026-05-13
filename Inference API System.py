from flask import Flask, request, jsonify
import joblib
app = Flask(__name__)
model = joblib.load('iris_model.pkl')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        prediction = model.predict([data['features']])
        return jsonify({'status': 'success', 'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)