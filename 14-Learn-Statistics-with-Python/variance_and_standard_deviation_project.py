import pandas as pd
import numpy as np
from weather_data import london_data


sns.barplot(x="month", y="TemperatureC", data=london_data, ax=ax0)
labels = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']


#Looking at temperature
temp = london_data["TemperatureC"]
average_temp = np.mean(temp)
temperature_var = np.var(temp)
temperature_standard_deviation = np.std(temp)
print(average_temp)
print(temperature_var)
print(temperature_standard_deviation)

#Filtering by month
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
print(np.mean(june))
print(np.mean(july))
print(np.std(june))
print(np.std(july))

#Every month
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
