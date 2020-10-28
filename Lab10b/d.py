# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  10b Program 4
# Date:        28 10 2020

import pandas as pd
# Thank god for pandas, that module makes this so much easier

df = pd.read_csv('WeatherDataWindows.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Maximum and minimum temperature
print(f"{'Maximum Temperature:':34} {df['Temp High'].max():6d} F")
print(f"{'Minimum Temperature:':34} {df['Temp Low'].min():6d} F")
print()

# Average daily precipitation
print(f"{'Average daily precipitation:':34} {df['Precipitation (in.)'].mean():6.3f} in.")
print()

# Percentage of days >= 90% humidity
print(f"{'Percentage of days >=90% humidity:':34} {len(df[df['Humidity High'] >= 90])/len(df)*100:6.2f} % of days")
print()

# Days of increasing dew point
print(f"{'Days of increasing dew point:':34} {len(df[df['Dew Point Avg'].diff() > 0]):6d} days")
print(f"{'Days of unchanging dew point:':34} {len(df[df['Dew Point Avg'].diff() == 0]):6d} days")
print(f"{'Days of decreasing dew point:':34} {len(df[df['Dew Point Avg'].diff() < 0]):6d} days")
