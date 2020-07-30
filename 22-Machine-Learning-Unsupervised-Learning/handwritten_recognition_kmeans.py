#import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use("TkAgg")

#Load data
digits = datasets.load_digits()

#K-Means clustering
model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)

#Plot cluster-centers
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')
for i in range(10):
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)


#sample data: 4444
new_samples = np.array([
[0.00,0.00,0.00,2.26,2.81,0.00,0.00,0.00,0.00,0.00,1.19,6.99,2.42,0.00,0.00,0.00,0.00,0.30,6.46,3.85,2.58,2.28,0.00,0.00,0.00,4.16,5.69,0.68,4.40,5.25,1.67,0.00,0.00,7.61,7.53,7.23,6.92,7.23,4.41,0.00,0.00,1.89,1.14,0.00,1.21,6.85,0.00,0.00,0.00,0.00,0.00,0.00,1.52,6.55,0.00,0.00,0.00,0.00,0.00,0.00,1.67,4.41,0.00,0.00],
[0.00,0.00,0.00,0.30,4.11,0.00,0.00,0.00,0.00,0.00,0.00,2.28,6.17,0.61,0.23,0.00,0.00,0.00,0.60,6.63,2.13,4.49,2.90,0.00,0.00,0.22,5.55,4.33,0.00,4.03,3.65,0.00,0.00,2.58,7.62,6.17,6.09,6.86,6.86,6.09,0.00,0.30,1.52,1.52,1.52,4.56,4.56,1.52,0.00,0.00,0.00,0.00,0.00,4.42,3.43,0.00,0.00,0.00,0.00,0.00,0.00,5.25,2.58,0.00],
[0.00,0.00,0.00,2.27,0.08,0.00,0.00,0.00,0.00,0.00,0.45,7.23,0.38,0.00,0.00,0.00,0.00,0.00,2.43,5.26,0.00,5.70,0.00,0.00,0.00,0.00,6.08,2.96,0.00,6.86,0.00,0.00,0.00,1.51,6.62,0.00,0.00,6.86,0.00,0.00,0.00,2.80,7.60,7.60,7.59,7.62,7.60,1.07,0.00,0.00,0.00,0.00,2.27,5.64,0.00,0.00,0.00,0.00,0.00,0.00,2.43,2.50,0.00,0.00],
[0.00,0.00,0.00,4.33,0.23,0.00,0.00,0.00,0.00,0.00,1.58,7.00,2.11,2.66,0.00,0.00,0.00,0.07,6.38,2.88,2.74,5.33,0.00,0.00,0.00,4.38,6.38,0.83,2.95,5.56,1.66,0.99,0.00,6.46,6.86,6.85,7.46,7.15,6.85,2.28,0.00,0.00,0.00,0.00,7.14,1.36,0.00,0.00,0.00,0.00,0.00,0.00,7.60,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.81,0.00,0.00,0.00]
])

#Predict
new_labels = model.predict(new_samples)
#Print number
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')

#Plot first 64 images
def plot():
  fig = plt.figure(figsize=(6, 6))
  fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
  # For each of the 64 images
  for i in range(64):
      # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position

      ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

      # Display an image at the i-th position

      ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

      # Label the image with the target value

      ax.text(0, 7, str(digits.target[i]))
plot()

plt.show()