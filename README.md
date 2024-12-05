# Dengue-Outbreak-Prediction-in-India

---

# Disease Outbreak Prediction and Precautions System

## 🚀 Project Overview

This project aims to predict disease outbreaks in vulnerable populations using environmental and healthcare indices. The system also provides actionable precautions to mitigate the risks associated with the predicted outbreaks. Built during [Hackathon Name], this project leverages **machine learning**, **Flask** for the backend, and a user-friendly **HTML/CSS** interface for interaction.

---

## 🌟 Features

1. **Disease Outbreak Prediction**:
   - Predicts the number of dengue cases based on temperature, rainfall, and healthcare index.
2. **Precautions and Mitigation**:
   - Displays a list of precautions tailored to the prediction.
3. **User-Friendly Interface**:
   - Clean and responsive web interface for seamless interaction.
4. **Data-Driven Insights**:
   - Analyzes historical data (2019–2023) to train the prediction model.

---

## 📂 Project Structure

```
project/
├── app.py                     # Main Flask application
├── data/
│   ├── disease_outbreaks_2019_to_2023.csv  # Dataset for training
│   ├── Dengue_Precautions_2019_2023_1.csv  # Precautions dataset
├── static/
│   ├── style.css              # CSS file for styling
├── templates/
│   ├── index.html             # Homepage for user input
│   ├── result.html            # Results page with prediction and precautions
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```

---

## 🛠️ Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Prepare the Data**:
   Ensure the datasets are present in the `data/` folder:

   - `disease_outbreaks_2019_to_2023.csv`
   - `Dengue_Precautions_2019_2023_1.csv`

3. **Run the Application**:
   Start the Flask development server:

   python app.py

4. **Access the Web App**:
   Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📊 Dataset

1. **Disease Data**:
   - Includes historical data on temperature, rainfall, healthcare index, and dengue cases (2019–2023).
2. **Precautions**:
   - A curated list of precautions and mitigation strategies.

---

## 🧠 Technology Stack

- **Backend**: Python (Flask), Pandas, Scikit-learn
- **Frontend**: HTML, CSS
- **Tools**: Jupyter Notebooks for analysis, GitHub for version control

---

## 🌐 Usage

1. Enter environmental and healthcare parameters (temperature, rainfall, healthcare index) in the input form.
2. Click **Predict** to get:
   - Predicted number of dengue cases.
   - List of precautions for mitigating disease outbreaks.

---

## 🎨 Screenshots

### Homepage

![Homepage Screenshot](images/home%20page.jpg)

### Prediction Results

![Results Screenshot](images/result%20page.jpg)

---

## 🤝 Team

- **(https://github.com/ASSASSINBAYEK/Dengue-outbreak-prediction-in-India)**
- [Team Member 1] - Jatin P Hegde
- [Team Member 2] - Aajna Rajesh Shetty
- [Team Member 3] - Vishnubhargav D
- [Team Member 4] - Kaviya R

---

## 📢 Acknowledgments

- [BMSCE Phaseshift Hackaphasia](https://registrations.phaseshift.bmsce.in/events/COMHAC) for organizing this event.
- Open-source libraries and datasets for enabling rapid development.
