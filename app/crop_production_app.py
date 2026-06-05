
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crop Production Analysis", layout="wide")

st.title("🌾 Improving Crop Production Using Data Science")
st.markdown("This application analyzes agricultural data to help improve crop production.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your Agriculture Data CSV file", type=["csv"])
if uploaded_file is not None:
    data_agri = pd.read_csv(uploaded_file)
    st.subheader("📊 Dataset Preview")
    st.dataframe(data_agri.head(70))

    # Display basic statistics
    st.subheader("📈 Basic Statistics")
    st.write(data_agri.describe())

    # Correlation heatmap
    st.subheader("🔍 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data_agri.corr(), annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

    # Column selection for custom plot
    st.subheader("📌 Custom Scatter Plot")
    numeric_cols = data_agri.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("X-Axis", options=numeric_cols, index=0)
        y_axis = st.selectbox("Y-Axis", options=numeric_cols, index=1)
        fig2, ax2 = plt.subplots()
        ax2.scatter(data_agri[x_axis], data_agri[y_axis], alpha=0.6)
        ax2.set_xlabel(x_axis)
        ax2.set_ylabel(y_axis)
        ax2.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig2)
    else:
        st.warning("Not enough numeric columns for plotting.")
else:
    st.info("Please upload a CSV file to begin.")
