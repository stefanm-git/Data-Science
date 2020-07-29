from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.use("TkAgg")

matplotlib.rcParams.update({'xtick.direction': 'in', 'ytick.direction': 'in',
                            'axes.grid': True, 'axes.grid.axis': 'x',
                            'axes.grid.which': 'major','grid.linewidth': 0.4,
                            'axes.linewidth': 2, })

#Load Data
emails = fetch_20newsgroups()
print(emails.target_names)

#Categories
category = emails.target_names
#print(emails.target[5])

acc = []
for i in range(len(category)):
  print(i)
  #Train data
  train_emails =  fetch_20newsgroups(
    categories=[category[i],'rec.sport.hockey'],
    subset='train',
    shuffle=True,
    random_state=108)

  #Test Data
  test_emails =  fetch_20newsgroups(
    categories=[category[i],'rec.sport.hockey'],
    subset='test',
    shuffle=True,
    random_state=108)

  counter = CountVectorizer()
  counter.fit(test_emails.data + train_emails.data)

  train_counts = counter.transform(train_emails.data)
  #print(train_counts)

  test_counts = counter.transform(test_emails.data)

  classifier = MultinomialNB()

  classifier.fit(train_counts, train_emails.target)

  acc.append(classifier.score(test_counts, test_emails.target))

#Plot result
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()
plt.subplots_adjust(bottom=0.44)
plt.plot(range(len(acc)), acc, marker='o', c='blue')
plt.title("Classifier Accuracy for Different Categories")
plt.xlabel("Category")
plt.ylabel("Validation Accuracy")
ax.set_xticks(range(len(acc)))
ax.set_xticklabels(category)
ax.tick_params(axis='x', rotation=90, labelsize=8)
ax.set_ylim([0.75, 1.05])
plt.show()

