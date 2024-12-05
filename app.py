from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load data
data = pd.read_csv("disease_outbreaks_2019_to_2023.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Prediction Logic
    X = data[['Temperature (°C)', 'Rainfall (mm)', 'Healthcare_Index']]
    y = data['Dengue_Cases']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict with user input
    user_input = request.form
    temperature = float(user_input['temperature'])
    rainfall = float(user_input['rainfall'])
    healthcare_index = float(user_input['healthcare_index'])
    prediction = model.predict([[temperature, rainfall, healthcare_index]])

    return render_template('result.html', prediction=int(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
