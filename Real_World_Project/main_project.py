import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 1. Load Real Data from a public URL (UCI Online Retail)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
print("Downloading real-world data... this might take a minute.")
df = pd.read_excel(url)

# 2. REAL-WORLD DATA CLEANING (The "Portfolio" Part)
# Remove cancelled orders (Invoice numbers starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
# Remove rows with no CustomerID
df.dropna(subset=['CustomerID'], inplace=True)
# Create a 'TotalSales' column
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# 3. Aggregating by Date to see Trends
df['Date'] = pd.to_datetime(df['InvoiceDate']).dt.date
daily_sales = df.groupby('Date')['TotalSales'].sum().reset_index()

# 4. Prepare for Machine Learning
# Convert dates to ordinal (numbers) so the model can read them
import datetime as dt
daily_sales['Date_Ordinal'] = pd.to_datetime(daily_sales['Date']).map(dt.datetime.toordinal)

X = daily_sales[['Date_Ordinal']]
y = daily_sales['TotalSales']

# Split data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train a Professional Model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# 6. Visualize the Real Results
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['Date'], daily_sales['TotalSales'], label='Actual Sales', color='teal')
plt.title('Real-World Daily Sales Trend (UK Retailer)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()