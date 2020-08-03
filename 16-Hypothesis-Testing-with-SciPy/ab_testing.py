import noshmishmosh
import numpy as np

#A/B Testing at Nosh Mish Mosh
#Baseline, Minimum Detectable Effect
#Statistical Significance

#Load data
all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
#Length of list
total_visitor_count = len(all_visitors)
paying_visitors_count = len(paying_visitors)
#Baseline: % of paying vistors to total visitors
baseline_percent = (paying_visitors_count * 100.0) / total_visitor_count
print('Baseline: '+str(baseline_percent))

#Minimum Detectable Effect
#How many typical purchases it would take to reach $1240 additional revenue
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240 / average_payment)
#Percent lift
percentage_point_increase = (new_customers_needed * 100.0) / total_visitor_count
print(percentage_point_increase)

minimum_detectable_effect = (percentage_point_increase * 100.0) / baseline_percent
print('Minimum Detectable Effect: '+str(minimum_detectable_effect))

print('Sample Size(Sign.: 90%) -> 290')