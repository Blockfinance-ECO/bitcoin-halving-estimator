from datetime import datetime, timedelta
from helpers import poipmf, bar_plot

# timestamp of last block
last_block_ts = 1709200548

# average interval between blocks in minutes
mu = 588.8077 / 60

# rate of events per unit of time
r = 1.0 / mu

# print(r)

current_block = 832522
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

estimate_start = datetime(2024, 4, 17, 0, 0, 0)
estimate_stop = datetime(2024, 4, 24, 0, 0, 0)

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
