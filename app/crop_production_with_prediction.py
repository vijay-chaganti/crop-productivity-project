
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Crop Production Analysis", layout="wide")

st.title("🌾 Improving Crop Production Using Data Science")
st.markdown("This application analyzes agricultural data and provides crop yield predictions using machine learning.")

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
    sns.heatmap(data_agri.select_dtypes(include='number').corr(), annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

    # Column selection for custom plot
    st.subheader("📌 Custom Scatter Plot")
    numeric_cols = data_agri.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("X-Axis", options=numeric_cols, index=0, key="x_axis")
        y_axis = st.selectbox("Y-Axis", options=numeric_cols, index=1, key="y_axis")
        fig2, ax2 = plt.subplots()
        ax2.scatter(data_agri[x_axis], data_agri[y_axis], alpha=0.6)
        ax2.set_xlabel(x_axis)
        ax2.set_ylabel(y_axis)
        ax2.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig2)
    else:
        st.warning("Not enough numeric columns for plotting.")

    # Prediction section
    st.subheader("🤖 Crop Yield Prediction")

    target_col = st.selectbox("Select Target Column (Yield)", options=numeric_cols, index=0)
    feature_cols = st.multiselect("Select Feature Columns", options=[col for col in numeric_cols if col != target_col])

    if feature_cols and target_col:
        X = data_agri[feature_cols]
        y = data_agri[target_col]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        st.write("**Model Evaluation:**")
        st.write(f"R² Score: {r2_score(y_test, y_pred):.2f}")
        st.write(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")

        st.markdown("### 🔮 Make a New Prediction")
        input_data = {}
        for feature in feature_cols:
            input_val = st.number_input(f"Enter value for {feature}", value=float(X[feature].mean()))
            input_data[feature] = input_val

        input_df = pd.DataFrame([input_data])
        if st.button("Predict Yield"):
            prediction = model.predict(input_df)[0]
            st.success(f"Predicted {target_col}: {prediction:.2f}")
else:
    st.info("Please upload a CSV file to begin.")
