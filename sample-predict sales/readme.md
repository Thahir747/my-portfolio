# Simple Sales Trend Predictor 📉

## 📌 Project Overview
This is a foundational Machine Learning project designed to demonstrate **Linear Regression**. The goal is to establish a baseline understanding of how sales grow over time and use that mathematical trend to predict future performance.

## 🛠 Technologies
- **Language:** Python
- **Libraries:** - `Pandas`: For structured data management.
  - `Scikit-Learn`: For implementing the Linear Regression model.
  - `Matplotlib`: For generating the trend visualization.

## 🧠 Key Concepts Covered

### 1. Simple Linear Regression
I utilized the formula:  
$$y = mx + b$$  
Where:
- **y**: Predicted Sales
- **x**: Month
- **m**: The growth rate (slope)
- **b**: The starting sales point (intercept)



### 2. Supervised Learning
This project is an example of Supervised Learning, where I provided the model with "Labeled Data" (past months and their corresponding sales) so it could learn the pattern and apply it to unseen future months.

## 📊 Results
The model successfully identified a positive growth trend across the 12-month period and provided calculated forecasts for Months 13, 14, and 15.

## 📂 Project Structure
- `sales_data.csv`: The historical dataset (12 months).
- `predict_sales.py`: The Python script containing the logic.
- `sales_chart.png`: A visual representation of the trend line vs. actual data.
