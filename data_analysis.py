import pandas as pd

data = pd.read_csv("students.csv")

print("\nStudent Data")
print(data)

average_grade = data["Grade"].mean()

print("\nAverage Grade:", average_grade)

highest_grade = data["Grade"].max()

print("Highest Grade:", highest_grade)
