import streamlit as st
import pandas as pd
import json
import os

# Load Configuration
config_path = os.path.join(os.getcwd(), 'config.json')
with open(config_path, 'r') as f:
    config = json.load(f)

# 1. Configure the Dashboard Canvas
st.set_page_config(page_title=config['business_name'], layout="wide")

# Header with Identity
st.title(f"⚡ {config['business_name']}")
st.subheader(f"Identity: {config['identity']}")
st.markdown(f"**Tone:** {config['tone']} | **Goal:** {config['conversion_goal']}")
st.markdown("---")

# 2. Render Data (Using Mock Data for now, ready for Scanner)
chart_data = pd.DataFrame({'Alpha': [1, 2, 3], 'Beta': [4, 5, 6]})
st.write("### Live System Metrics")
st.line_chart(chart_data)
