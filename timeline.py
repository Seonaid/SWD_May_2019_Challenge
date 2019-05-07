import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

# Add a timeline to my twitter chart
# Original code from https://matplotlib.org/gallery/lines_bars_and_markers/timeline.html

events = {'Joined Twitter':'2010-02-20',
          'Post A Day Blog Challenge':'2011-01-01',
          'Cross-Canada Voyage':'2011-07-30',
          'India (no wifi)':'2012-11-30',
          'Joined Instagram':'2014-10-26',
          'Installed Social Media Blocker':'2016-01-22',
          'Summer on the Road':'2018-07-15'}

names, dates = events.keys(), events.values()

dates = [datetime.strptime(ii, "%Y-%m-%d") for ii in dates]



# Next, we'll iterate through each date and plot it on a horizontal line. We'll add some styling to the text so that overlaps aren't as strong.

# Note that Matplotlib will automatically plot datetime inputs.

def add_timeline(axis):
    levels = np.array([5, 220, 20, 20, 170, 70, 15])
    ax = axis
    # fig, ax = plt.subplots(figsize=(10, 6))

    # Create the base line
    start = min(dates)
    stop = max(dates)
    ax.plot((start, stop), (220, 220), 'k', alpha=.5)

    # Iterate through releases annotating each one
    for ii, (iname, idate) in enumerate(zip(names, dates)):
        level = levels[ii]

        ax.scatter(idate, 220, s=100, facecolor='w', edgecolor='k', zorder=9999)
        # Plot a line up to the text
        ax.plot((idate, idate), (220, level), c='r', alpha=.7)
        # Give the text a faint background and align it properly
        ax.annotate(iname, (idate, level), xytext=(idate, 230),
                fontsize=12,
                backgroundcolor=(1., 1., 1., .3), rotation=45, rotation_mode='anchor')

