# Bitcoin Halving Estimator

Required data:

1. Most recent block timestamp
2. Average block time

## Theory

Using the Poisson process

https://en.wikipedia.org/wiki/Poisson_distribution

Computing the distribution at each minute each date (of given range), summing over and normalizing.

## Results

```sh
$ python poisson.py 
last block mined 2024-01-05 12:02:08
12/04 1.0697157672442134e-08
13/04 6.568467914508807e-06
14/04 0.0008886228396629344
15/04 0.028041903735466014
16/04 0.21982989356400623
17/04 0.4538692448409959
18/04 0.2559581149800536
19/04 0.039708523038799536
20/04 0.0016779863793498682
21/04 1.913145659375473e-05
```

and bar plot

![bar_plot](https://github.com/Blockfinance-ECO/bitcoin-halving-estimator/blob/main/res.png?raw=true)
