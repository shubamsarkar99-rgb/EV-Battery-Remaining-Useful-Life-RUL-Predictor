# 🔋 EV Battery Remaining Useful Life (RUL) Prediction & Simulation

An end-to-end Machine Learning web application designed to simulate and predict the **Remaining Useful Life (RUL)** of Electric Vehicle (EV) lithium-ion batteries based on operational parameter analysis.

---

## 📸 App Dashboard Preview

![EV Battery Simulation Dashboard](./assets/photo.png)


---

## 📌 Project Overview

Battery degradation analysis is crucial for EV safety and performance optimization. This project utilizes machine learning algorithms (trained on battery charge/discharge cycles) to predict remaining lifecycle capacity in real-time through an interactive Streamlit user interface.

### **Key Features:**
- **Real-Time Simulation:** Live parameter inputs for Voltage, Current, Temperature, Capacity, and operational cycles.
- **Trained ML Model:** Powered by a tuned `GradientBoostingRegressor` model trained during Project 2.
- **Interactive UI:** Built using Streamlit for fast parameter testing and clear visual outputs.

---

## 📁 Project Structure

```text
ev-battery-streamlit-app/
│
├── app.py                 # Streamlit web application frontend & logic
├── model.pkl              # Trained GradientBoostingRegressor model file
├── venv/                  # Local Python virtual environment
└── README.md              # Project documentation
```

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.11+
- **Framework:** Streamlit
- **Machine Learning:** Scikit-Learn, NumPy
- **Model Serialization:** Pickle / Joblib

---

## 🚀 How to Run Locally

### 1. Clone or Open Project Directory
Navigate to your project root folder:
```bash
cd ev-battery-streamlit-app
```

### 2. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 3. Install Dependencies (If not installed)
```bash
pip install streamlit scikit-learn numpy
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` to view the running dashboard.

---

## 📊 Model Details

- **Model Type:** GradientBoostingRegressor
- **Features (8 Inputs):** Voltage (V), Current (A), Temperature (°C), Current Capacity (Ah), and operational status indicators.
- **Target Variable:** Remaining Useful Life (RUL in Cycles)

**made by SHUBAM SARKAR**