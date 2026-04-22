import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load the data
df = pd.read_csv('sales_data.csv')

# 2. Prepare the data for the model
# X = Month (Input), y = Sales (What we want to predict)
X = df[['Month']] 
y = df['Sales']

# 3. Create and Train the "Brain" (Linear Regression Model)
model = LinearRegression()
model.fit(X, y)

# 4. Predict sales for the next 3 months (Months 13, 14, 15)
future_months = [[13], [14], [15]]
predictions = model.predict(future_months)

print(f"Predicted Sales for Month 13: {predictions[0]:.2f}")
print(f"Predicted Sales for Month 14: {predictions[1]:.2f}")
print(f"Predicted Sales for Month 15: {predictions[2]:.2f}")

# 5. Visualize it!
plt.scatter(X, y, color='blue', label='Actual Sales') # Show dots for real data
plt.plot(X, model.predict(X), color='red', label='Trend Line') # Show the line the AI built
plt.title('Sales Trend Prediction')
plt.xlabel('Month')
plt.ylabel('Sales (INR)')
plt.legend()
plt.show()  