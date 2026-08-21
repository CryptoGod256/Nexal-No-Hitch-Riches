import sys
# Force the dashboard to look in the system folder where pandas is installed
sys.path.append("/data/data/com.termux/files/usr/lib/python3.13/site-packages")

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Nexal Engine", layout="wide")
st.title("Nexal Engine: Live Dashboard")
st.success("Decentralized Retainer Active. Welcome to the Engine. 🤞✅🌎🤲💰")

st.subheader("Data Flow Visualization (System Test)")
st.write("Intercepting mock data streams to verify visualization capabilities...")

# Generate test data to prove Pandas and Numpy are working
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Data Node A", "Data Node B", "Data Node C"]
)

st.line_chart(chart_data)
