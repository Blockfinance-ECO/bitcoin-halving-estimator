# Bitcoin Halving Estimator

## ⚠️ DISCLAIMER ⚠️

THIS SCRIPT COMES WITH ABSOLUTELY NO GUARANTEE OF CORRECTNESS AND BY USING IT OR DATA IT PROVIDES YOU AGREE TO TAKE FULL RESPONSIBILITY OF ALL THE DECISIONS MADE.

## Input data

1. Most recent block timestamp
2. Average block time

## Theory

Using the Poisson process

https://en.wikipedia.org/wiki/Poisson_distribution

Computing the distribution at each minute each date (of given range), summing over and normalizing.

## Results

```sh
$ python poisson.py 
last block mined 2024-01-28 12:09:51
17/04 0.00013980407783522532
18/04 0.011156454543201392
19/04 0.1626784826721654
20/04 0.47860653358099275
21/04 0.3040300538689585
22/04 0.042142848103684044
23/04 0.0012458231531628271
```

and bar plot

![bar_plot](https://github.com/Blockfinance-ECO/bitcoin-halving-estimator/blob/master/res.png?raw=true)

as well as hourly estimate

![bar_plot_hourly](https://github.com/Blockfinance-ECO/bitcoin-halving-estimator/blob/master/res_hourly.png?raw=true)
