import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NYC Recycling Dashboard", layout="wide")

summary = pd.read_csv('cache/borough_capture_summary.csv')

boroughs = sorted(summary['BOROUGH'].unique())
selected_borough = st.sidebar.selectbox("Choose a Borough", boroughs)

filtered = summary[summary['BOROUGH'] == selected_borough]

st.title("♻️ NYC Recycling Capture Rate Dashboard")
st.subheader(f"Average Capture Rate by Year — {selected_borough}")

fig, ax = plt.subplots()
ax.plot(filtered['YEAR'], filtered['AVG_CAPTURE_RATE'], marker='o')
ax.set_xlabel("Year")
ax.set_ylabel("Avg Capture Rate")
ax.set_title(f"{selected_borough} — Yearly Average Capture Rate")
ax.grid(True)
plt.xticks(rotation=45)

st.pyplot(fig)

if st.checkbox("Show data table"):
    st.dataframe(filtered)