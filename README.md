# csc368-a1
scripts used for csc368 a1

## Exploration 1
- input sizes from 1k to 10k to 100k

## Exploration 2
- keep input size at 100k
- change the in-order to out-of-order pipeline

## Exploration 3
- keep input size at 100k
- default: 4kB L1D, 4kB L1I, 32kB L2, L1D associativity 2, L1I associativity 2, L2 associativity 8
- 5 runs
  -   Exploration 1 with a size 100k no changes
  -   L2 cache size change from 32kB to 64kB
  -   L1 cache size from 4kB to 8kB for both L1 instruction cache and L1 data cache
  -   L1 associativity change to 4 for both L1 instruction cache and L1 data cache
  -   L2 associativity change from 8 to 16  

