import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv("dataset/student-mat.csv", sep=";")

print("First Rows:")
print(df.head())
print("Rows and Columns:", df.shape)
print("Data Info:")
print(df.info())
print("Descriptive Statistics:")
print(df.describe())
print("Missing Values:")
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

avg_grade = df['G3'].mean()
print("Average Final Grade =", round(avg_grade,2))

above_15 = (df['G3'] > 15).sum()
print("Students Scoring Above 15 =", above_15)

corr = df['studytime'].corr(df['G3'])
print("Correlation =", round(corr,3))

gender_perf = df.groupby('sex')['G3'].mean()
print(gender_perf)

#---------------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(df['G3'],
         bins=10,
         edgecolor='black')

plt.title("Distribution of Final Grades")
plt.xlabel("Grade")
plt.ylabel("Frequency")

plt.show()

plt.figure(figsize=(8,5))

plt.scatter(df['studytime'],
            df['G3'])

plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")

plt.show()

gender_perf.plot(kind='bar')

plt.title("Average Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")

plt.show()

