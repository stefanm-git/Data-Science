import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'xtick.direction': 'in', 'ytick.direction': 'in',
                            'axes.linewidth': 1.5, })

data = pd.read_csv("country_data.csv")
#print(data.head())

#Quantiles
life_expectancy = data["Life Expectancy"]

life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
print(life_expectancy_quartiles)


#GDP
gdp = data['GDP']
median_gdp = np.quantile(gdp, 0.5)
print(median_gdp)

#Split
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] >= median_gdp]
low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25, 0.5, 0.75])

#Plot
bin = 30
fig = plt.figure(figsize=(8, 7), dpi=100)
plt.subplots_adjust(hspace=.2, wspace=0.25)
ax0 = fig.add_subplot(211)
ax1 = fig.add_subplot(223)
ax2 = fig.add_subplot(224)

#0
ax0.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP",bins=bin)
ax0.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP", bins=bin)
ax0.set_xlabel("Age")
ax0.set_ylabel("Count")
ax0.set_title("Life Expectancy splitted by GDP")
ax0.legend()

#1
ax1.hist(gdp, bins=bin, label="GDP")
ax1.set_xlabel("GDP")
ax1.set_ylabel("Count")
ax1.legend()

#2
ax2.hist(life_expectancy, bins=bin, label="Life Expectancy")
ax2.set_xlabel("Age")
ax2.set_ylabel("Count")
ax2.legend()

plt.show()


