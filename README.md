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
last block mined 2024-02-29 10:55:48
17/04 1.485421099862189e-05
18/04 0.007436569889166641
19/04 0.22919854835833886
20/04 0.5993048016455322
21/04 0.16003598657505616
22/04 0.004000837355541634
23/04 8.401965365866516e-06
```

and bar plot

![bar_plot](https://github.com/Blockfinance-ECO/bitcoin-halving-estimator/blob/master/res.png?raw=true)

as well as hourly estimate

![bar_plot_hourly](https://github.com/Blockfinance-ECO/bitcoin-halving-estimator/blob/master/res_hourly.png?raw=true)
