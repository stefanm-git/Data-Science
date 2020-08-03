import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency


#Import Vein Pack lifespan
vein_pack_lifespans = familiar.lifespans(package='vein')
#1-Sample T-Test
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
#P-value significance test
if vein_pack_test.pvalue < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack is Probably Good For You Somehow!")

#Import Artery Pack lifespan
artery_pack_lifespans = familiar.lifespans(package="artery")
#2-Sample T-Test
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
#P-value significance test
if package_comparison_results.pvalue < 0.05:
  print("The Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is also a great product!")

#Survey data iron counts
iron_contingency_table = familiar.iron_counts_for_package()
#print iron_contingency_table
#Chi-Squared test
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)
#P-value significance test
if iron_pvalue < 0.05:
  print("The Artery Pack Is Proven To Make You Live Longer!")
else:
  print("The Artery Pack is Probably Good For You Somehow!")
