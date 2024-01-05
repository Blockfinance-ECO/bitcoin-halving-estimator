from scipy.stats import poisson
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

def bar_plot(
        labels, values,
        ylabel=None, xlabel=None, title=None, filename=None, yscale='linear', transparent=False):
    fig, ax = plt.subplots()


    ax.bar(labels, values, zorder=10)

    ax.set_yscale(yscale)

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    plt.xticks(rotation=45)

    ax.set_title(title)
    ax.grid(zorder=5)

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

# timestamp of last block
last_block_ts = 1704452528

# average interval between blocks in minutes
mu = 572.707 / 60

# rate of events per unit of time
r = 1.0 / mu

# print(r)

current_block = 824453
halving_interval = 210000

# get the next halving block

halving = 0
while halving < current_block:
    halving += halving_interval

# number of blocks that need to pass to halving
k = halving - current_block

# compute the distribution
now = datetime.fromtimestamp(last_block_ts) # datetime.now()
print('last block mined', now)

estimate_start = datetime(2024, 4, 12, 0, 0, 0)
estimate_stop = datetime(2024, 4, 22, 0, 0, 0)

probs = []
dates = []

t = (estimate_start - now).total_seconds() / 60
dt = estimate_start
daily_p = 0.0
tot_p = 0.0
while dt < estimate_stop:
    dtt = dt + timedelta(minutes=1)
    t += 1
    p = poipmf(r, t, k)
    daily_p += p
    if dtt.day != dt.day:
        probs.append(daily_p)
        dates.append(dt.strftime('%d/%m'))
        tot_p += daily_p
        daily_p = 0.0
    dt = dtt

# normalize
for j in range(len(probs)):
    probs[j] = probs[j]/tot_p

# print results
for p, d in zip(probs, dates):
    print(d, p)

# plot
bar_plot(
    dates, probs,
    ylabel='$P$',
    xlabel='date',
    title='BTC halving probability estimate using Poisson process',
    filename='res.png')
