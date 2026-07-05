import pandas as pd
import numpy as np

# 1. Generate realistic time-series data (100 days of sales)
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
sales_data = {
    'Date': dates,
    'Store_A': np.random.normal(500, 50, 100),
    'Store_B': np.random.normal(450, 60, 100)
}
df = pd.DataFrame(sales_data)

# 2. Add some artificial missing values and an outlier
df.loc[10:14, 'Store_A'] = np.nan
df.loc[85, 'Store_B'] = 2000.0

# 3. Clean the data (Interpolate missing, cap outliers)
df['Store_A'] = df['Store_A'].interpolate(method='linear')
q_high = df['Store_B'].quantile(0.95)
df['Store_B'] = np.where(df['Store_B'] > q_high, q_high, df['Store_B'])

# 4. Feature Engineering: Extract Day of Week
df['DayOfWeek'] = df['Date'].dt.day_name()
df['Is_Weekend'] = df['Date'].dt.dayofweek.isin([5, 6])

# 5. Calculate 7-day rolling averages for trend analysis
df['Store_A_7d_avg'] = df['Store_A'].rolling(window=7).mean()
df['Store_B_7d_avg'] = df['Store_B'].rolling(window=7).mean()

# 6. Calculate day-over-day percentage growth for Store A
df['Store_A_Pct_Growth'] = df['Store_A'].pct_change() * 100

# 7. Aggregate data: Average sales by Day of Week
weekly_seasonality = df.groupby('DayOfWeek')[['Store_A', 'Store_B']].mean()
best_days = weekly_seasonality.sort_values(by='Store_A', ascending=False)

# 8. Print the aggregated results and the final tail of the dataset
print(best_days.head(3))
print(df[['Date', 'Store_A', 'Store_A_7d_avg']].tail())