import sys
import os

# Dynamic venv site-packages path resolution
current_dir = os.path.dirname(os.path.abspath(__file__))
venv_lib = os.path.join(current_dir, '.venv', 'lib')

if os.path.exists(venv_lib):
    for py_ver in os.listdir(venv_lib):
        site_packages = os.path.join(venv_lib, py_ver, 'site-packages')
        if os.path.exists(site_packages) and site_packages not in sys.path:
            sys.path.insert(0, site_packages)

import streamlit as st
import pickle
import os
import numpy as np

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

st.title("🔋 EV Battery Remaining Useful Life (RUL) Prediction")
st.write("Project 3: Live Simulation Dashboard")

# Load Pickle Model
@st.cache_resource
def load_model():
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

try:
    model = load_model()
    st.success("✅ Model Successfully Loaded!")

    st.header("Enter Battery Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        f1 = st.number_input("Feature 1 (Voltage)", value=3.71)
        f2 = st.number_input("Feature 2 (Current)", value=2.01)
        f3 = st.number_input("Feature 3 (Temperature)", value=25.02)
        f4 = st.number_input("Feature 4 (Capacity)", value=2.55)
        
    with col2:
        f5 = st.number_input("Feature 5", value=1.0)
        f6 = st.number_input("Feature 6", value=1.0)
        f7 = st.number_input("Feature 7", value=1.0)
        f8 = st.number_input("Feature 8", value=1.0)

    if st.button("Predict RUL"):
        input_features = np.array([[f1, f2, f3, f4, f5, f6, f7, f8]])
        prediction = model.predict(input_features)
        st.success(f"Estimated Remaining Useful Life: **{prediction[0]:.2f} Cycles**")

except Exception as e:
    st.error(f"Model Load Error: {e}")