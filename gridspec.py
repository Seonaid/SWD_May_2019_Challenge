import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


# demo 3 : gridspec with subplotpars set.

def create_subplots():
    fig = plt.figure(figsize=(11, 9))

    fig.suptitle('Tweet Confessions')
    fig.text(0.5, 0.92, "May SWD Challenge: Curate your own data set. \nI chose my own twitter feed from the very beginning of my account.", horizontalalignment='center', wrap=True)

    gs1 = GridSpec(5, 2, hspace=0.6)
    # gs1.update(left=0.05, right=0.98, top =0.95)
    ax1 = plt.subplot(gs1[:-2, :])
    ax2 = plt.subplot(gs1[-2:, :-1])
    ax3 = plt.subplot(gs1[-2:, -1])

    return fig, ax1, ax2, ax3

# gs2 = GridSpec(3, 3)
# gs2.update(left=0.55, right=0.98, hspace=0.05)
# ax4 = plt.subplot(gs2[:, :-1])
# ax5 = plt.subplot(gs2[:-1, -1])
# ax6 = plt.subplot(gs2[-1, -1])

#make_ticklabels_invisible(fig)

# plt.show()