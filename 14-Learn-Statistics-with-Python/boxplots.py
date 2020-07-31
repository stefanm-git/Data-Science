import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

print(healthcare.head())

#print(healthcare["DRG Definition"].unique())
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
#print(chest_pain)

alabama_chest_pain = chest_pain[chest_pain['Provider State']=='AL']
#print(alabama_chest_pain)

cost = alabama_chest_pain[' Average Covered Charges '].values
#print(cost)

#plt.boxplot(cost)
#plt.show()

states = chest_pain['Provider State'].unique()
#print(states)

dataset = []
for state in states:
  dataset.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

plt.figure(figsize=(15, 4))
plt.boxplot(dataset, labels = states)
plt.xlabel("State")
plt.ylabel('Average Covered Charges')

plt.show()
