# 🏠 Mumbai House Price Predictor

This is a machine learning web application that predicts the price (in Lakhs) of a house in Mumbai based on user inputs like area, BHK, region, and property attributes.

## 🔍 Project Overview

This application allows users to:
- Choose a locality (region) in Mumbai.
- Enter area in square feet.
- Select BHK (number of bedrooms).
- Choose construction status and age of the property.
- Predict the price using a trained Random Forest Regression model.

## 📊 Tech Stack

- **Frontend**: HTML, CSS, Jinja2
- **Backend**: Python, Flask
- **ML Model**: Random Forest Regressor (Scikit-learn)
- **Data Handling**: Pandas, NumPy
- **Deployment**: Flask local server


## 🧠 Model Training Summary

- **Input Features**: BHK, Area (sqft), Region, Status, Age
- **Target**: Price in Lakh
- **Encoding**: LabelEncoding for categorical variables
- **Outliers**: Removed using domain knowledge and percentile rules

## 💡 How to Run Locally

1. **Clone this repository:**
```bash
git clone https://github.com/your-username/Mumbai_House_Price_Predictor.git
cd Mumbai_House_Price_Predictor

## 🏃🏽‍♂️ To Run the App
```bash
python app.py

Visit http://127.0.0.1:5000 in your browser.

