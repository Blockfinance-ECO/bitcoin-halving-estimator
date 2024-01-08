from scipy.stats import poisson
import matplotlib.pyplot as plt

def bar_plot(
        labels, values,
        ylabel=None,
        xlabel=None,
        title=None,
        filename=None,
        yscale='linear',
        transparent=False,
        every_nth_label=None, figsize=None, bottom=None):
    # default figsize is [6.4, 4.8]
    fig, ax = plt.subplots(figsize=figsize)

    if bottom is not None:
        fig.subplots_adjust(bottom=bottom)

    ax.bar(labels, values, zorder=10)

    ax.set_yscale(yscale)

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    plt.xticks(rotation=45)

    ax.set_title(title)
    ax.grid(zorder=5)

    if every_nth_label is not None:
        for j, label in enumerate(ax.get_xticklabels()):
            if j % every_nth_label == 0:
                plt.setp(label, visible=True)
            else:
                plt.setp(label, visible=False)

    if filename is not None:
        plt.savefig(filename, transparent=transparent)
    else:
        plt.show()

def poipmf(r, t, k):
    lambda_ = r*t
    rv = poisson(lambda_)
    return rv.pmf(k)

def poicdf(r, t, k):
    lambda_ = r*t
    rv = poisson(lambda_)
    return rv.cdf(k)
