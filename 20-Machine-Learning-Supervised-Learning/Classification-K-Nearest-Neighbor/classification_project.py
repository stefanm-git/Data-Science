#import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import numpy as np
breast_cancer_data = load_breast_cancer()

#Inspect data
#print(breast_cancer_data)
#print(breast_cancer_data.data[0])
#print(breast_cancer_data.feature_names)
#print(breast_cancer_data.target)
#print(breast_cancer_data.target_names)

#Create training/validation data
training_data , validation_data, training_labels, validation_labels = train_test_split(
breast_cancer_data.data,
breast_cancer_data.target,
test_size=0.2,
random_state=80
)

#Validation accuracy over nearest neigbor
k_n = []
for k in range(1, 100):
  classifier = KNeighborsClassifier(n_neighbors=k)
  classifier.fit(training_data, training_labels)

  #print(classifier.score(validation_data, validation_labels))
  k_n.append(classifier.score(validation_data, validation_labels))

#plt.figure(figsize=(14.5, 8.5), dpi=80)

plt.plot(range(len(k_n)), k_n,  alpha=1)
plt.title("Classifier Accuracy")
plt.xlabel("Nearest Neighbour")
plt.ylabel("Validation Accuracy")


plt.show()