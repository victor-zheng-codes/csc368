# csc368-a2
scripts used for csc368 a2

## Exploration 1: Prefetching
- input sizes at 100k

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

## Exploration 2: Branch Prediction
- keep input size at 100k
- change the in-order to out-of-order pipeline

### Metrics additional on top of 
 - Out-Of-Order Specific Metrics
  - Issue rate: system.cpu.issueRate
  - FUBusy Rate: system.cpu.fuBusyRate
    
## Results Documentation


## Generating Input
- HIST
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/sequenceData/randomSeq -t int -r 256 <n> <filepath>`
  - n=1000, 10000, 100000
  - chosen default distribution generates a random sequence of n integers in the range of [0:256]

- WC
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/sequenceData/trigramString <n> <filepath>`
  - n=1000, 10000, 100000
  - chosen distribution generates a random sequence of n trigram strings

- MIS
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/graphData/randLocalGraph -j -d 3 -m <10n> <n> <filepath>`
  - n=1000, 10000, 100000
  - chosen distribution generates a random local graph with approximately n vertices and 10n edges

- SORT
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/sequenceData/randomSeq -t double <n> <filepath>`
  - n=1000, 10000, 100000
  - chosen distribution generates Double-precision floating-point numbers uniformly at random from the range [0:1]

- DDUP
  - `/u/csc368h/winter/pub/workloads/pbbsbench/testData/sequenceData/randomSeq -t int -r <n> <n> <filepath>`
  - n=1000, 10000, 100000
  - chosen distribution generates A random sequence of n integers in the range [0:n)
    
## Running Workload
- HIST
  - running the sequential executable since we are on single core
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt -d <m5outdir> <script> -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/histogram/sequential/histogram -i <filepath>`
- WC
  - running the serial executable instead of histogram since we are on a single core
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt -d <m5outdir> <script> -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/wordCounts/serial/wc -i <filepath>`

- MIS
  - running the serial executable since we are on single core
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt -d <m5outdir> <script> -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/maximalIndependentSet/serialMIS/MIS -i <filepath>`

- SORT
  -  running the sampleSort algorithm
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt -d <m5outdir> <script> -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/comparisonSort/sampleSort/sort -i <filepath>`

- DDUP
  - running the serial hash executable
  - e.g. `/u/csc368h/winter/pub/bin/gem5.opt -d <m5outdir> <script> -b /u/csc368h/winter/pub/workloads/pbbsbench/benchmarks/removeDuplicates/serial_hash/dedup -i <filepath>`
