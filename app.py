from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

app = Flask(__name__)

# Load data
data = pd.read_csv('disease_outbreaks_2019_to_2023.csv')
precautions_data = pd.read_csv('Dengue_Precautions_2019_2023_1.csv')  # Load precautions

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
    try:
        temperature = float(user_input['temperature'])
        rainfall = float(user_input['rainfall'])
        healthcare_index = float(user_input['healthcare_index'])

        # Ensure all inputs are non-negative
        if temperature < 0 or rainfall < 0 or healthcare_index < 0:
            return render_template(
                'result.html',
                prediction=None,
                precautions=None,
                error="Input values must be non-negative. Please try again."
            )
        
        prediction = model.predict([[temperature, rainfall, healthcare_index]])
        prediction = max(0, int(prediction[0]))  # Ensure no negative predictions

    except ValueError:
        return render_template(
            'result.html',
            prediction=None,
            precautions=None,
            error="Invalid input. Please enter numeric values."
        )

    # Get Precautions (Add logic to fetch relevant rows if necessary)
    precautions = precautions_data['Precautions'].tolist()

    return render_template('result.html', prediction=prediction, precautions=precautions, error=None)

if __name__ == '__main__':
    app.run(debug=True)
