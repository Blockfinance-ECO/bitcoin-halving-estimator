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
last block mined 2024-01-08 10:23:34
19/04 0.0003364912800734537
20/04 0.013638496278878743
21/04 0.14350182239877776
22/04 0.41417933219677
23/04 0.34120760599558747
24/04 0.08142180790257529
25/04 0.0056041267524674955
26/04 0.00011031719486980381
```

and bar plot

![bar_plot](https://github.com/Blockfinance-ECO/bitcoin-halving-estimator/blob/master/res.png?raw=true)

as well as hourly estimate

![bar_plot_hourly](https://github.com/Blockfinance-ECO/bitcoin-halving-estimator/blob/master/res_hourly.png?raw=true)
