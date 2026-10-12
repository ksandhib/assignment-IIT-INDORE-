import pandas as pd

# Load the CSV file
churn = pd.read_csv("customer_churn.csv")

# Task 2
newCols = churn.iloc[:, [2, 6, 8, 19]]
print("Task 2 - Selected Columns:\n", newCols.head(), "\n")

# Task 3
subset_200_1000 = churn.loc[200:1000, :]
print("Task 3 - Rows 200 to 1000:\n", subset_200_1000.head(), "\n")

# Task 4
subset_20_199_cols = churn.iloc[20:200, 2:16]
print("Task 4 - Rows 20 to 199 & Columns 2 to 15:\n", subset_20_199_cols.head(), "\n")

# Task 5
top_100 = churn.head(100)
print("Task 5 - Top 100 Records:\n", top_100.head(), "\n")

# Task 6
last_10 = churn.tail(10)
print("Task 6 - Last 10 Records:\n", last_10, "\n")

# Task 7
last_record = churn.tail(1)
print("Task 7 - Last Record:\n", last_record, "\n")

# Task 8
sorted_by_tenure = churn.sort_values(by='tenure', ascending=False)
print("Task 8 - Sorted by Tenure (Descending):\n", sorted_by_tenure.head(), "\n")

# Task 9a
cond1 = churn[(churn['tenure'] > 50) & (churn['gender'] == 'Female')]
print("Task 9a - Tenure > 50 and Female:\n", cond1, "\n")

# Task 9b
cond2 = churn[(churn['gender'] == 'Male') & (churn['SeniorCitizen'] == 0)]
print("Task 9b - Male and Not Senior Citizen:\n", cond2, "\n")

# Task 9c
cond3 = churn[(churn['TechSupport'] == 'Yes') & (churn['Churn'] == 'No')]
print("Task 9c - TechSupport = Yes and Churn = No:\n", cond3, "\n")

# Task 9d
cond4 = churn[(churn['Contract'] == 'Month-to-month') & (churn['Churn'] == 'Yes')]
print("Task 9d - Contract = Month-to-month and Churn = Yes:\n", cond4, "\n")

# Task 10
count = 0
for _, row in churn.iterrows():
    if (row['gender'] == 'Male') and (row['SeniorCitizen'] == 1) and (row['TechSupport'] == 'Yes'):
        count += 1
print("Task 10 - Male Senior Citizens with Tech Support:", count)
