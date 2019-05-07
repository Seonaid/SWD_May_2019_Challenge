import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

# Add a timeline to my twitter chart
events = {'Post A Day Challenge':'2011-01-01',
          'Cross-Canada Voyage':'2011-07-01',
          'India':'2012-11-05',
          'UIT':'2014-09-01',
          'Joined Instagram':'2014-10-26',
          'Summer on the Road':'2018-07-15'}

names, dates = events.keys(), events.values()

dates = [datetime.strptime(ii, "%Y-%m-%d") for ii in dates]



# Next, we'll iterate through each date and plot it on a horizontal line. We'll add some styling to the text so that overlaps aren't as strong.

# Note that Matplotlib will automatically plot datetime inputs.

levels = np.array([-5, 5, -3, 3, -1, 1])
fig, ax = plt.subplots(figsize=(8, 5))

# Create the base line
start = min(dates)
stop = max(dates)
ax.plot((start, stop), (0, 0), 'k', alpha=.5)

# Iterate through releases annotating each one
for ii, (iname, idate) in enumerate(zip(names, dates)):
    level = levels[ii % 6]
    vert = 'top' if level < 0 else 'bottom'

    ax.scatter(idate, 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
    # Plot a line up to the text
    ax.plot((idate, idate), (0, level), c='r', alpha=.7)
    # Give the text a faint background and align it properly
    ax.text(idate, level, iname+str(level),
            horizontalalignment='right', verticalalignment='top', fontsize=14,
            backgroundcolor=(1., 1., 1., .3), rotation=90)
ax.set(title="Matplotlib release dates")
# Set the xticks formatting
# format xaxis with 3 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=3))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
fig.autofmt_xdate()

# Remove components for a cleaner look
plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
          list(ax.spines.values())), visible=False)
plt.show()