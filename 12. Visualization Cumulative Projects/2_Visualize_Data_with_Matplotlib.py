import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(8, 8), dpi=100)
plt.subplots_adjust(hspace=1.3)
ax0 = fig.add_subplot(311)
ax1 = fig.add_subplot(312)
ax2 = fig.add_subplot(313)


"Bar Chart"
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

ax0.bar(range(len(games)), viewers, color='slateblue')
ax0.legend(["Twitch"])
ax0.set_title('Featured Game Viewers')
ax0.set_xlabel('Games')
ax0.set_ylabel('Viewers')
ax0.set_xticks(range(0, 10))
ax0.set_xticklabels(games, rotation=30)


"Pie Chart"
ax1.axis('equal')
ax1.axis('off')
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.004, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ax1.pie(countries, explode=explode, colors=colors, shadow=False, startangle=345, autopct='%1.0f%%', pctdistance=1.3, frame=True, radius=.07, textprops={'fontsize': 9})

ax1.set_title("League of Legends Viewers' Whereabouts",  y=1.3)
ax1.legend(labels, loc="right")


"Line Chart"
hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

ax2.set_title("Time Series")
ax2.set_xlabel("Hour")
ax2.set_ylabel("Viewers")
ax2.plot(hour, viewers_hour)
ax2.legend(['2015-01-01'])
ax2.set_xticks(hour)
ax2.set_yticks([0, 20, 40, 60, 80, 100, 120])

y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

ax2.fill_between(hour, y_lower, y_upper, alpha=0.2)

plt.show()
