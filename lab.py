# Employee Salary EDA Assignment
import pandas as pd

#Task 1 - LOAD THE DATASET 
df = pd.read_csv("employee_salary.csv")
print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())
print("\nDataset Shape (Rows, Columns):")
print(df.shape)
print("\nTotal Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

#Task 2 - DISPLAY METADATA OBJECTIVE
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nDataset Information:")
df.info()
print("\nDescriptive Statistics:")
print(df.describe())
print("\nAverage Salary:")
print(df["Salary"].mean())
print("\nStandard Deviation of Numerical Columns:")
print(df.std(numeric_only=True))
print("\nFeature with Highest Standard Deviation:")
print(df.std(numeric_only=True).idxmax())

#Task 3 - CHECK MISSING VALUES OBJECTIVE
print("\nMissing Values:")
print(df.isnull().sum())
print("\nPercentage of Missing Values:")
print((df.isnull().sum() / len(df)) * 100)
print("\nColumn with Maximum Missing Values:")
print(df.isnull().sum().idxmax())
print("\nNumber of Duplicate Records:")
print(df.duplicated().sum())
print("\nDataset Size Before Cleaning:", len(df))
df = df.drop_duplicates()
print("Dataset Size After Cleaning:", len(df))