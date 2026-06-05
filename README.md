# 🌾 CropCast — Crop Productivity Prediction

A Machine Learning project to predict crop productivity using historical agricultural data from India.

## 📌 Project Overview
- Analyzes agricultural data from 2011-2015
- Predicts crop yield using multiple ML algorithms
- Interactive dashboard and Streamlit web app

## 🤖 ML Models Used
- Linear Regression
- Decision Tree
- Random Forest
- Logistic Regression
- K Nearest Neighbours (KNN)

## 📁 Project Structure
crop-productivity-project/
│
├── 📂 app/
│   ├── crop_production_app.py              # Basic Streamlit app
│   └── crop_production_with_prediction.py  # Full ML prediction app
│
├── 📂 dashboard/
│   └── crop_productivity_prediction_dashboard.html  # Interactive dashboard
│
├── 📂 data/
│   ├── Agriculture-Data.csv          # Crop yield data 2011-2015
│   ├── DATA.csv                      # India state-wise data (246k rows)
│   ├── Seasonal-Data.csv             # Season wise data
│   ├── Yearly-Production.csv         # Year wise production
│   └── cleaned_agriculture_data.csv  # Cleaned dataset
│
├── 📂 notebooks/
│   ├── 01_Data_Loading_and_Cleaning.ipynb
│   ├── 02_EDA_and_Visualization.ipynb
│   ├── 03_Linear_Regression.ipynb
│   ├── 04_Decision_Tree_Random_Forest.ipynb
│   ├── 05_Logistic_Regression.ipynb
│   ├── 06_KNN_Model.ipynb
│   └── 07_Data_AnalysisAPY_Dataset.ipynb
│
├── requirements.txt
└── README.md
---

## 📊 Dataset Information
| Dataset | Rows | Columns | Description |
|---|---|---|---|
| Agriculture-Data.csv | 57 | 18 | Crop yield 2011-2015 |
| DATA.csv | 246,091 | 7 | State-wise crop production |
| Seasonal-Data.csv | — | — | Season wise breakdown |
| Yearly-Production.csv | — | — | Year wise production |

---

## 🚀 How to Run Locally
1. Clone the repository:
```bash
   git clone https://github.com/yourusername/crop-productivity-project.git
```
2. Create virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run the app:
```bash
   streamlit run app/crop_production_with_prediction.py
```

---

## 🛠️ Technologies Used
- **Python 3.10**
- **Pandas & NumPy** — Data manipulation
- **Seaborn & Matplotlib** — Data visualization
- **Scikit-learn** — Machine learning models
- **Streamlit** — Web application
- **Jupyter Notebook** — Analysis & modeling

---

## 👨‍💻 Author
VIJAY CHAGANTI — CT UNIVERSITY