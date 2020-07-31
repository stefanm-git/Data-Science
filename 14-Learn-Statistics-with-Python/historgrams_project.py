import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
bin = 100
plt.figure(1)
plt.subplot(211)

plt.hist(flights, range=(0, 365), bins=bin, edgecolor="k")

plt.title("Yearly Frequency of Visitors")
plt.xlabel(("Days (1 day increments)"))
plt.ylabel("Count")

plt.subplot(212)
plt.hist(in_bloom, range=(0, 365), bins=bin, edgecolor="k")

plt.title("Flower Blooms by day")
plt.xlabel(("Days (1 day increments)"))
plt.ylabel("Bloom Count")

plt.tight_layout()

plt.show()