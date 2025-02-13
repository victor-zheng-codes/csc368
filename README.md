# csc368-a1
scripts used for csc368 a1

## Exploration 1
- input sizes from 1k to 10k to 100k

### Metrics Chosen
- Execution Time
  - simSeconds
- Number of Instructions
  - simInsts
  - simOps
  - system.cpu.fetchStats0.branchRate
  - system.cpu.commitStats0.numFPInsts
  - system.cpu.commitStats0.numIntInsts
  - system.cpu.numCycles 
- Cache hits and cache misses
  - system.cpu.l1d.overallHits
  - system.cpu.l1d.overallMisses
  - system.cpu.l1d.overallMissRate
  - system.cpu.l1i.overallHits
  - system.cpu.l1i.overallMisses
  - system.cpu.l1i.overallMissRate
  - system.l2_cache.overallHits
  - system.l2_cache.overallMisses
  - system.l2_cache.overallMissRate
- CPI
  - system.cpu.cpi
- Instruction Mix
  - system.cpu.commitStats0.numInsts
  - system.cpu.commitStats0.committedInstType::IntAlu
  - system.cpu.commitStats0.committedInstType::(depend on benchmark)

## Exploration 2
- keep input size at 100k
- change the in-order to out-of-order pipeline

### Metrics additional
 - Out-Of-Order Specific Metrics
  - Issue rate: system.cpu.issueRate
  - FUBusy Rate: system.cpu.fuBusyRate
    
## Exploration 3
- keep input size at 100k
- default: 4kB L1D, 4kB L1I, 32kB L2, L1D associativity 2, L1I associativity 2, L2 associativity 8
- Exploration 1 with a size 100k no changes in-order
- Exploration 2 with a size 100k no changes out-of-order
- 4 runs, two each for in-order and out-of-order pipelines
  -   L1 cache size from 4kB to 8kB for both L1 instruction cache and L1 data cache
  -   L1 associativity change to 4 for both L1 instruction cache and L1 data cache

## Results Documentation
Available here: https://docs.google.com/spreadsheets/d/1spE-UH5s1P_3Kw6wnODC7X6j8q7kPJKTxZ4-5oUYX30/edit?usp=sharing

## Generating Input
- HIST
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/sequenceData/randomSeq -t int -r 256 n ./data/sequence/rand-256-n`
  - n=1000, 10000, 100000
  - chosen default distribution generates a random sequence of n integers in the range of [0:256]

- WC
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/sequenceData/trigramString n ./data/sequence/trigram-string-n`
  - n=1000, 10000, 100000
  - chosen distribution generates a random sequence of n trigram strings

- MIS
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/graphData/randLocalGraph -j -d 3 -m <10n> <n> ./data/graph/<filename>`
  - n=1000, 10000, 100000
  - chosen distribution generates a random local graph with approximately n vertices and 10n edges
    
## Running Workload
- HIST
  - running the sequential executable since we are on single core
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt -d m5outdir a1-e1-system.py -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/histogram/sequential/histogram -i ./data/sequence/rand-256-1000`
- WC
  - running the serial executable instead of histogram since we are on a single core
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt -d m5out-wordcount-1000 a1-e1-system.py -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/wordCounts/serial/wc -i ../sequenceData/trigram-string-1000`

- MIS
  - running the serial executable since we are on single core
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt <script> -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/maximalIndependentSet/serialMIS/MIS -i ./data/graph/<filename>`
