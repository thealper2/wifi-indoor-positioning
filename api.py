import os
import pickle

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH = "rf.pkl"
model = pickle.load(open(MODEL_PATH, "rb"))

@app.route('/get_room', methods=['POST'])
def upload_apk_and_get_data():
    signal = request.json['signal']
    print(signal)

    result = model.predict([signal])
    labels = ["balcony", "bathroom", "bedroom", "kitchen", "living_room"]

    
    return jsonify({'room': labels[result]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)