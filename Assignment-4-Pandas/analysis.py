import pandas as pd


df = pd.read_csv('customer_churn.csv')


print("🔷 Sorted by tenure (descending):")
print(df.sort_values(by='tenure', ascending=False))


print("\n🔶 Tenure > 50 and Gender = Female:")
print(df[(df['tenure'] > 50) & (df['Gender'] == 'Female')])

print("\n🔶 Gender = Male and SeniorCitizen = 0:")
print(df[(df['Gender'] == 'Male') & (df['SeniorCitizen'] == 0)])


print("\n🔶 TechSupport = Yes and Churn = No:")
print(df[(df['TechSupport'] == 'Yes') & (df['Churn'] == 'No')])

print("\n🔶 Contract = Month-to-month and Churn = Yes:")
print(df[(df['Contract'] == 'Month-to-month') & (df['Churn'] == 'Yes')])
