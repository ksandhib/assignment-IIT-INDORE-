import pandas as pd

# Load the CSV file
churn = pd.read_csv("customer_churn.csv")

# Task: Select rows from index 0 to 3 (since your dataset has only 4 rows)
# and columns from index 2 to 15
subset = churn.iloc[0:4, 2:16]

# Print output to terminal
print("Assignment 2 – Pandas Output:\n")
print(subset)
