from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
region_encoder = joblib.load('region_encoder.pkl')
status_encoder = joblib.load('status_encoder.pkl')
age_encoder = joblib.load('age_encoder.pkl')

# Load list of all regions (optional: from training data or directly from encoder)
all_regions = list(region_encoder.classes_)

@app.route('/')
def home():
    return render_template('index.html', regions=all_regions)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    region = request.form['region']
    area = float(request.form['area'])
    bhk = int(request.form['bhk'])
    status = request.form['status']
    age = request.form['age']

    # Encode categorical values
    region_encoded = region_encoder.transform([region])[0]
    status_encoded = status_encoder.transform([status])[0]
    age_encoded = age_encoder.transform([age])[0]

    # Prepare input array
    input_data = np.array([[bhk, area, region_encoded, status_encoded, age_encoded]])

    # Predict price
    prediction = model.predict(input_data)[0]
    prediction = round(prediction, 2)

    return render_template('index.html', prediction=prediction, regions=all_regions)

if __name__ == '__main__':
    app.run(debug=True)
