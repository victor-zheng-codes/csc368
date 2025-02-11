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
  - system.cpu.commitStats0.numFPInsts
  - system.cpu.commitStats0.numIntInsts
  - system.cpu.numCycles 
- Cache hits and cache misses
  - system.cpu.l1d.overallHits
  - system.cpu.l1d.overallMisses
  - system.l2_cache.overallHits
  - system.l2_cache.overallMisses
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

