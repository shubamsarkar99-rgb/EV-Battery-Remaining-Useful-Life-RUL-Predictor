# 🔋 EV Battery Remaining Useful Life (RUL) Prediction

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.6.1-F7931E?style=for-the-badge&logo=scikitlearn)

An interactive Machine Learning dashboard built with Streamlit to simulate and predict the **Remaining Useful Life (RUL)** of Electric Vehicle (EV) batteries based on operational parameters.

---

## 📸 Dashboard Preview

![EV Battery Simulation Dashboard](./assets/photo.png)

---

## 🎯 Project Overview

This application acts as the **Simulation & Deployment Interface (Project 3)** for the EV Battery RUL Prediction system. It consumes a trained machine learning model exported from Google Colab and allows users to input live battery parameter values to estimate remaining charge cycles.

### Key Features
* ⚡ **Real-time Prediction**: Instant RUL calculation using Gradient Boosting Regressor.
* 🎛️ **Multi-Parameter Input**: Adjust Voltage, Current, Temperature, Capacity, and internal health metrics.
* 🛠️ **Seamless Integration**: Loads pre-trained model artifacts (`model.pkl`) without cloud latency.

---

## 🛠️ Project Structure

```text
ev-battery-rul-predictor/
├── .venv/                      # Python Virtual Environment
├── assets/                     # Media & Screenshots
│   └── photo.png              # Dashboard Preview Image
├── app.py                      # Streamlit Application Script
├── model.pkl                   # Trained ML Model (Scikit-Learn 1.6.1)
├── README.md                   # Project Documentation
└── requirements.txt            # Dependencies List
