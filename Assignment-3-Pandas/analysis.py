import pandas as pd


df = pd.read_csv('customer_churn.csv')


print("🟢 Top 100 records:")
print(df.head(100))


print("\n🟠 Last 10 records:")
print(df.tail(10))


print("\n🔴 Last record:")
print(df.tail(1))
