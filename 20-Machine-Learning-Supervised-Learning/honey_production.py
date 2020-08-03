import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#Figure
fig = plt.figure(figsize=(8, 8), dpi=100)
plt.subplots_adjust(hspace=.8)
ax0 = fig.add_subplot(311)
ax1 = fig.add_subplot(312)
ax2 = fig.add_subplot(313)

#Read data
df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
print(df)
#Mean of total production per year
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
#print(prod_per_year)

#x-values
X = prod_per_year['year']
X = X.values.reshape(-1, 1)
#y-values
y = prod_per_year['totalprod']

#0
ax0.scatter(X,y)
ax0.set_title("Honey Production Data")
ax0.set_xlabel('Year')
ax0.set_ylabel('Honey Prodcution')

#Linear Regression model
regr = linear_model.LinearRegression()
regr.fit(X,y)
print(regr.coef_[0])
print(regr.intercept_)
y_predict = regr.predict(X)

#1
ax1.plot(X, y_predict)
ax1.scatter(X,y)
ax1.set_title("Honey Production Linear Fit")
ax1.set_xlabel('Year')
ax1.set_ylabel('Honey Prodcution')

#Prediction
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)
future_predict = regr.predict(X_future)

#2
ax2.plot(X, y_predict)
ax2.plot(X_future, future_predict)
ax2.scatter(X,y)
ax2.set_title("Honey Production Prediction")
ax2.set_xlabel('Year')
ax2.set_ylabel('Honey Prodcution')


plt.show()