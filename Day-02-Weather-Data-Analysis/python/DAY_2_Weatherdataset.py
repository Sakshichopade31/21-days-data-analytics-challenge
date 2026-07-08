import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:\Users\Vivek\Downloads\1. Weather Data.csv")

"""
print(data)
print("First 5 rows of the dataset:")
print(data.head())
print("Shape of the dataset:")
print(data.shape)   
print("Index of the dataset:")
print(data.index)
print("Columns of the dataset:")
print(data.columns)
print("Data types of the dataset:")
print(data.dtypes)
print("Summary statistics of the dataset:")
print(data.describe())
print("Information about the dataset:")
print(data.info())
print("Unique values in weather condition column:")
print(data['Weather'].unique())
print("Number of unique values in weather condition column:")
print(data['Weather'].nunique())
print("Unique values in each column:")
for column in data.columns:
    print(f"{column}: {data[column].nunique()}")



print("Count total number of non-null values in the dataset:")
print(data.count())
print("Value counts of weather condition column:")
print(data['Weather'].value_counts())
"""

#FIND ALL UNIQUE VALUES IN "WIND SPEED" VALUES IN DATA  COLUMN
"""
print("Unique values in 'Wind Speed' column:")
print(data['Wind Speed_km/h'].unique())
print("Number of unique values in 'Wind Speed' column:")
print(data['Wind Speed_km/h'].nunique())
"""
#FIND THE NUMBER OF TIMES WHEN "WEATHER IS CLEAR" IN DATASET
#VALUE_COUNTS() (method 1)
"""
print(data['Weather'].value_counts())
"""
#filtering data when weather is clear (method 2)
"""
clear_weather_data = data[data['Weather'] == 'Clear']  
print("Number of times when weather is clear:", clear_weather_data.shape[0])
"""
#grouping data by weather condition and counting occurrences (method 3)
"""
weather_counts = data.groupby('Weather').size()
print("Number of times when weather is clear:", weather_counts['Clear'])
"""

#Find the  number of times when "Wind Speed is exactly 4 km/h"
"""
wind_speed_4_data = data[data['Wind Speed_km/h'] == 4]
print("Number of times when wind speed is exactly 4 km/h:", wind_speed_4_data.shape[0])
"""
#shape[0] gives the number of rows in the filtered data

#fins the null values in the dataset
#using isnull() and sum() methods
"""
null_values = data.isnull().sum()
print("Null values in each column:")
print(null_values)
"""
#rename the column name weather to weather_condition

data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)
print(data.head())


#what is the mean value of "Visibility" in this dataset
"""
print("Mean value of Visibility in the dataset:")
print(data.Visibility_km.mean()) # Mean of the entire Visibility_km column
"""

#what is the standard deviation of "Pressure" in this dataset
"""
print("Standard deviation of Pressure in the dataset:")
print(data.Press_kPa.std()) # Standard deviation of the entire Press_kPa column
"""

#what is the variance of "Relative Humidity" in this dataset
"""
print("Variance of Relative Humidity in the dataset:")
print(data['Rel Hum_%'].var()) # Variance of the entire Rel Hum_% column
"""

#Find all instances when "Snow" was recorded 
"""

print("Instances when 'Snow' was recorded:")
"""

#by filtering the data using str.contains() method 1
#str.contains() method is used to check if a string contains a specific substring, in this case, 'Snow'.
# The case=False argument makes the search case-insensitive, and na=False ensures that NaN values are not included in the results.
"""

snow_data = data[data['Weather Condition'].str.contains('Snow', case=False, na=False)]
print(snow_data)
"""

#by using value_counts() method 2
"""
print("Mean value of Visibility in the dataset:")
"""
# Ensure 'Visibility_km' is numeric (coerce non-numeric to NaN) before aggregating.
"""
data['Visibility_km'] = pd.to_numeric(data['Visibility_km'], errors='coerce')
"""

# Compute mean only for the Visibility_km column to avoid dtype issues in other columns.
"""
print("Number of instances when 'Snow' was recorded:", data['Weather Condition'].value_counts()['Snow']) 
"""
#by using groupby() method 3
"""
snow_counts = data.groupby('Weather Condition').size()
print("Number of instances when 'Snow' was recorded:", snow_counts['Snow'])
"""
#by filtering
"""
snow_filtered_data = data[data['Weather Condition'] == 'Snow']
print("Number of instances when 'Snow' was recorded:", snow_filtered_data.shape[0])
"""
#Find all instances when "Wind Speed is above 24" and "Visibility is  25"
"""
wind_visibility_data = data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
print("Instances when Wind Speed is above 24 and Visibility is 25:")
print(wind_visibility_data.to_string(index=False)) 
"""
# to_string() method is used to print the entire DataFrame without truncation, 
# and index=False prevents printing the index column.

#What is the mean value of each column against each "Weather Condition"
"""
print("Mean value of each column against each Weather Condition:")
print(data.groupby('Weather Condition').mean(numeric_only=True).to_string())
"""

#WHAT IS THE MINIMUM & MAXIMUM VALUE OF EACH COLUMN AGAINST EACH "WEATHER CONDITION"
"""
print("Minimum value of each column against each Weather Condition:")
print(data.groupby('Weather Condition').min(numeric_only=True).to_string())
print("Maximum value of each column against each Weather Condition:")
print(data.groupby('Weather Condition').max(numeric_only=True).to_string())
"""
#SHOW ALL THE RECORDS WHERE "WEATHER CONDITION IS FOG"
"""
fog_data = data[data['Weather Condition'] == 'Fog']
print("Records where Weather Condition is Fog:")
print(fog_data.to_string(index=False))
"""

#FIND ALL RECORDS WHERE "WEATHER CONDITION IS CLEAR" OR "VISIBILITY IS ABOVE 40"
"""
clear_or_high_visibility_data = data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]
print("Records where Weather Condition is Clear or Visibility is above 40:")
print(clear_or_high_visibility_data.to_string(index=False))
"""

#FIND ALL RECORDS WHERE "WEATHER CONDITION IS CLEAR" AND "RELATIVE HUMIDITY IS ABOVE 50"
#OR VISIBILITY IS ABOVE 40
"""
clear_humidity_visibility_data = data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]
print("Records where Weather Condition is Clear and Relative Humidity is above 50 or Visibility is above 40:")
print(clear_humidity_visibility_data.head(50).to_string(index=False))  # Displaying only the first 50 records for brevity
"""

#1. Weather Conditions Count (Bar Chart)
weather_counts = data['Weather Condition'].value_counts()

plt.figure(figsize=(12,6))
weather_counts.plot(kind='bar')

plt.title("Weather Condition Frequency")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#--------------------------------------------------------------
#2. Wind Speed Distribution (Histogram)
plt.figure(figsize=(8,5))

plt.hist(data['Wind Speed_km/h'], bins=20)

plt.title("Distribution of Wind Speed")
plt.xlabel("Wind Speed (km/h)")
plt.ylabel("Frequency")

plt.show()

#--------------------------------------------------------------
#3. Visibility Distribution
plt.figure(figsize=(8,5))

plt.hist(data['Visibility_km'], bins=15)

plt.title("Visibility Distribution")
plt.xlabel("Visibility (km)")
plt.ylabel("Frequency")

plt.show()

#--------------------------------------------------------------
#4. Temperature vs Humidity (Scatter Plot)
plt.figure(figsize=(8,6))

plt.scatter(data['Temp_C'], data['Rel Hum_%'])

plt.title("Temperature vs Relative Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Relative Humidity (%)")

plt.show()

#--------------------------------------------------------------
#5. Mean Temperature of Every Weather Condition
mean_temp = data.groupby('Weather Condition')['Temp_C'].mean()

plt.figure(figsize=(12,6))

mean_temp.plot(kind='bar')

plt.title("Average Temperature for Each Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Average Temperature")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
#--------------------------------------------------------------
#6. Mean Visibility of Every Weather Condition
mean_visibility = data.groupby('Weather Condition')['Visibility_km'].mean()

plt.figure(figsize=(12,6))

mean_visibility.plot(kind='bar')

plt.title("Average Visibility for Each Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Visibility (km)")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
#--------------------------------------------------------------
#7. Mean Wind Speed for Every Weather Condition
mean_wind = data.groupby('Weather Condition')['Wind Speed_km/h'].mean()

plt.figure(figsize=(12,6))

mean_wind.plot(kind='bar')

plt.title("Average Wind Speed by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Wind Speed (km/h)")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
#--------------------------------------------------------------
#8. Pressure Distribution
plt.figure(figsize=(8,5))

plt.hist(data['Press_kPa'], bins=20)

plt.title("Pressure Distribution")
plt.xlabel("Pressure (kPa)")
plt.ylabel("Frequency")

plt.show()
#--------------------------------------------------------------
#9. Weather Condition Pie Chart
weather_counts = data['Weather Condition'].value_counts().head(8)

plt.figure(figsize=(8,8))

plt.pie(weather_counts,
        labels=weather_counts.index,
        autopct='%1.1f%%')

plt.title("Top 8 Weather Conditions")

plt.show()
#--------------------------------------------------------------
#10. Correlation Heatmap (Most Important)
import matplotlib.pyplot as plt

corr = data.corr(numeric_only=True)

plt.figure(figsize=(8,6))

plt.imshow(corr, cmap='coolwarm')

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.show()
#--------------------------------------------------------------
#11. Wind Speed vs Visibility
plt.figure(figsize=(8,6))

plt.scatter(data['Wind Speed_km/h'],
            data['Visibility_km'])

plt.title("Wind Speed vs Visibility")
plt.xlabel("Wind Speed")
plt.ylabel("Visibility")

plt.show()
#--------------------------------------------------------------
#12. Temperature Distribution
plt.figure(figsize=(8,5))

plt.hist(data['Temp_C'], bins=20)

plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

plt.show()
#--------------------------------------------------------------
#13. Relative Humidity Distribution
plt.figure(figsize=(8,5))

plt.hist(data['Rel Hum_%'], bins=15)

plt.title("Relative Humidity Distribution")
plt.xlabel("Humidity (%)")
plt.ylabel("Frequency")

plt.show()
#--------------------------------------------------------------
#14. Top 10 Highest Wind Speeds
top10 = data.nlargest(10, 'Wind Speed_km/h')

plt.figure(figsize=(10,5))

plt.bar(top10.index.astype(str),
        top10['Wind Speed_km/h'])

plt.title("Top 10 Highest Wind Speeds")
plt.xlabel("Record")
plt.ylabel("Wind Speed")

plt.show()
#--------------------------------------------------------------
#15. Mean Values of All Numeric Columns
means = data.mean(numeric_only=True)

plt.figure(figsize=(8,5))

means.plot(kind='bar')

plt.title("Mean of Numeric Columns")

plt.xticks(rotation=45)

plt.show()
#------------------------------------------------------
