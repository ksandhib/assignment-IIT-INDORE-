import pandas as pd


df = pd.read_csv('customer_churn.csv')


count = 0


for index, row in df.iterrows():
    if (
        row['TechSupport'] == 'Yes' and 
        row['Gender'] == 'Male' and 
        row['SeniorCitizen'] == 1
    ):
        count += 1

print(f"📌 Number of male senior citizens with Tech Support: {count}")
