import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

#Load data
rottweiler_t1 = fetchmaker.get_tail_length("rottweiler")
print(np.mean(rottweiler_t1))
print(np.std(rottweiler_t1))

#Data to rescue
whippet_rescue = fetchmaker.get_is_rescue("whippet")
#Get the number of entries in whippet_rescue that are 1
num_whippet_rescues = np.count_nonzero(whippet_rescue)
#Get the number of samples in the whippet set
num_whippets = np.size(whippet_rescue)
#Binomal test
print('Binomal test: '+str(binom_test(num_whippet_rescues, num_whippets, 0.08)))

#Significant difference in the average weights of the three dog breeds?
#ANOVA (analysis of variance), comperative numerical test
w = fetchmaker.get_weight("whippet")
t = fetchmaker.get_weight("terrier")
p = fetchmaker.get_weight("pitbull")
print('ANOVA: '+str(f_oneway(w, t, p).pvalue))

#Which of the pairs of the dog breeds differ from each other
#Turkey's Range Test
values = np.concatenate([w, t, p])
labels = ['whippet'] * len(w) + ['terrier'] * len(t) + ['pitbull'] * len(p)
print(pairwise_tukeyhsd(values, labels, .05))

#Categorial dog test, significantly different color breakdowns
#SciPys Chi Square test
poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

color_table = [
  [
    np.count_nonzero(poodle_colors == "black"),
    np.count_nonzero(shihtzu_colors == "black")
  ],
  [
    np.count_nonzero(poodle_colors == "brwown"),
    np.count_nonzero(shihtzu_colors == "brown")
  ],
  [
    np.count_nonzero(poodle_colors == "gold"),
    np.count_nonzero(shihtzu_colors == "gold")
  ],
  [
    np.count_nonzero(poodle_colors == "grey"),
    np.count_nonzero(shihtzu_colors == "grey")
  ],
  [
    np.count_nonzero(poodle_colors == "white"),
    np.count_nonzero(shihtzu_colors == "white")
  ],
]
print(color_table)

_, color_pval, _, _ = chi2_contingency(color_table)
print(color_pval)