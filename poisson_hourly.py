from datetime import datetime, timedelta
from helpers import poipmf, bar_plot

# timestamp of last block
last_block_ts = 1706440191

# average interval between blocks in minutes
mu = 588.2566 / 60

# rate of events per unit of time
r = 1.0 / mu

# print(r)

current_block = 827781
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
    if dtt.hour != dt.hour:
        probs.append(daily_p)
        dates.append(dt.strftime('%d/%m %H:%M'))
        tot_p += daily_p
        daily_p = 0.0
    dt = dtt

# normalize
for j in range(len(probs)):
    probs[j] = probs[j]/tot_p

# print results
for p, d in zip(probs, dates):
    print(d, p)

nb_x = 3

# plot
bar_plot(
    dates, probs,
    ylabel='$P$',
    xlabel='date',
    title='BTC halving hourly probability estimate using Poisson process',
    filename='res_hourly.png', every_nth_label=4, figsize=(6.4*nb_x, 4.8), bottom=0.2)
