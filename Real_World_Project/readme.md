# Real-World Sales Trend Prediction 📈

## 📌 Project Overview
This project focuses on predicting daily sales trends for a UK-based online retailer using a dataset of over 500,000 transactions. Unlike simple linear models, this project tackles real-world challenges like missing values, cancelled orders, and non-linear growth patterns.

## 🛠 Technologies & Tools
- **Language:** Python 3.x
- **Environment:** VS Code
- **Data Manipulation:** `Pandas` (for cleaning and aggregating 500k+ rows)
- **Machine Learning:** `Scikit-Learn` (Random Forest Regressor)
- **Visualization:** `Matplotlib`
- **Data Source:** UCI Machine Learning Repository (Online Retail Dataset)

## 🧪 Data Science Workflow

### 1. Data Cleaning (The Most Critical Step)
Real-world data is messy. In this project, I:
- **Removed Anomalies:** Filtered out "Cancelled" transactions (Invoice numbers starting with 'C').
- **Handled Missing Values:** Removed records with missing Customer IDs to ensure data integrity.
- **Derived Features:** Created a `TotalSales` column by calculating `Quantity * UnitPrice`.

### 2. Feature Engineering
- Converted `InvoiceDate` from a string into a datetime object.
- Aggregated sales by day to find the "Daily Sales" trend.
- Converted dates into **Ordinal format** so the Machine Learning model could interpret time as a numerical input.

### 3. Predictive Modeling
I chose the **Random Forest Regressor** over a simple Linear Regression because:
- It handles "outliers" (random sales spikes) much better.
- It is an "Ensemble" method, meaning it uses multiple decision trees to find the most accurate prediction.



## 📊 Key Results
- Successfully visualized a 12-month sales cycle.
- Identified significant volatility in daily sales, typical of retail environments.
- The model provides a baseline for inventory planning and revenue forecasting.

## 🚀 How to Run
1. Clone this repository.
2. Install dependencies: `pip install pandas matplotlib scikit-learn openpyxl`.
3. Run the script: `python main_project.py`.
