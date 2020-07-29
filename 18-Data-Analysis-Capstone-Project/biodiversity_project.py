from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
matplotlib.use("TkAgg")
from scipy.stats import chi2_contingency
from matplotlib.gridspec import GridSpec

"set format"
colors = ['sienna', 'red', 'green', 'blue', 'orange', 'cyan', 'yellow']
matplotlib.rcParams.update({'xtick.direction': 'in', 'ytick.direction': 'in',
                            'axes.grid': True, 'axes.grid.axis': 'both',
                            'axes.grid.which': 'major','grid.linewidth': 0.4,
                            'axes.linewidth': 2, })

"Figure"
fig = plt.figure(figsize=(14.5, 8.5), dpi=80)
gs = GridSpec(3, 4, figure=fig, hspace=0.5, wspace= 0.1, right= 0.78, )
ax0 = fig.add_subplot(gs[0, :3])
ax01 = fig.add_subplot(gs[0, 3:4])
ax1 = fig.add_subplot(gs[1, :3])
ax11 = fig.add_subplot(gs[1, 3:4])
ax2 = fig.add_subplot(gs[2, :3])
ax21 = fig.add_subplot(gs[2, 3:4])

"print format"
pd.options.display.width=None

"read csv species"
species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace=True)
species.groupby('conservation_status').scientific_name.nunique().reset_index()
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')

"Conservation Status by Species"
"Bar"
labels = protection_counts.conservation_status.values
ax0.bar(range(len(protection_counts)),
        protection_counts.scientific_name.values, color=colors)
ax0.set_xticks(range(len(protection_counts)))
ax0.tick_params(axis='x', rotation=0)
ax0.set_xticklabels(labels)
ax0.set_ylabel('Number of Species')
ax0.set_title('Conservation Status by Species')
"Pie"
ax01.pie(protection_counts.scientific_name.values, radius=1.2,
        shadow=True, startangle=90, colors = colors)
handles = []
for i, l in enumerate(labels):
    handles.append(matplotlib.patches.Patch(color=colors[i], label=l))
ax0.legend(handles,labels, bbox_to_anchor=(1.3,1.025), loc="upper left")



species['is_protected'] = species.conservation_status != 'No Intervention'
category_counts = species.groupby(['category', 'is_protected'])\
                         .scientific_name.nunique().reset_index()
category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name')\
                                .reset_index()
category_pivot.columns = ['category', 'not_protected', 'protected']
category_pivot['percent_protected'] = (category_pivot.protected / \
                                      (category_pivot.protected + category_pivot.not_protected))*100

"Protection in [%] by Category"
"Bar"
labels = category_pivot.category.values
ax1.bar(range(len(category_pivot)),
        category_pivot.percent_protected.values, color=['black', 'red', 'green', 'blue', 'orange', 'cyan'],)
ax1.set_xticks(range(len(category_pivot)))
ax1.tick_params(axis='x', rotation=0)
ax1.set_xticklabels(labels)
ax1.set_ylabel('Protected [%]')
ax1.set_title('Protection in [%] by Category')
"Pie"
ax11.pie(category_pivot.percent_protected.values, radius=1.2,
        shadow=True, startangle=90, colors = colors, autopct='%1.1f%%',
         pctdistance=1.30,)
handles = []
for i, l in enumerate(labels):
    handles.append(matplotlib.patches.Patch(color=colors[i], label=l))
ax11.legend(handles,labels, bbox_to_anchor=(1.1,1.3), loc="upper left")


"Chi Test"
contingency = [[30, 146],
               [5, 73]]
print('contigency', chi2_contingency(contingency))


"read csv observation"
observations = pd.read_csv('observations.csv')

species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
sheep_observations = observations.merge(sheep_species)
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()


"Observations of Sheep per Week"
"Bar"
labels = obs_by_park.park_name.values
ax2.bar(range(len(obs_by_park)),
        obs_by_park.observations.values, color=['black', 'red', 'green', 'blue', 'orange', 'cyan'])
ax2.set_xticks(range(len(obs_by_park)))
ax2.tick_params(axis='x', rotation=10, labelsize=9)
ax2.set_xticklabels(labels)
ax2.set_ylabel('Number of Observations')
ax2.set_title('Observations of Sheep per Week')
"Pie"
ax21.pie(obs_by_park.observations.values, radius=1.2,
        shadow=True, startangle=90, colors = colors, autopct='%1.1f%%',
         pctdistance=1.30,)
handles = []
for i, l in enumerate(labels):
    handles.append(matplotlib.patches.Patch(color=colors[i], label=l))
ax21.legend(handles,labels, bbox_to_anchor=(1.0,.9), loc="upper left")



minimum_detectable_effect = 100 * 0.05 / 0.15
print(minimum_detectable_effect)

baseline = 15
sample_size_per_variant = 870
bryce = 870 / 250.
print(bryce)

yellowstone = 810 / 507.
print(yellowstone)

plt.subplots_adjust(hspace=0.5)
plt.show()