import m5
import argparse
from m5.objects import *
import sys

# 100k, modify the cache configs

DEAFULT_BINARY = '/u/csc368h/winter/pub/workloads/hello'

# Add argparse command line processing
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--binary', type=str, default= DEAFULT_BINARY)
parser.add_argument('-f', '--frequency', type=str, default='1GHz')
parser.add_argument('-o', '--outFile')
parser.add_argument('-i', '--inFile')
args = parser.parse_args()


class L1ICache(Cache):
    assoc = 2
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 8
    tgts_per_mshr = 20
    size= '1kB'

class L1DCache(Cache):
    assoc = 2
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 8
    tgts_per_mshr = 20
    size='1kB'

class L2Cache(Cache):
    assoc = 8
    tag_latency = 8
    data_latency = 8
    response_latency = 1
    mshrs = 8
    tgts_per_mshr = 20
    size='32kB'


# System creation
system = System()

## gem5 needs to know the clock and voltage
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = args.frequency
system.clk_domain.voltage_domain = VoltageDomain() # defaults to 1V

## Create a crossbar so that we can connect main memory and the CPU (below)
system.membus = SystemXBar()
system.system_port = system.membus.cpu_side_ports

## Use timing mode for memory modelling
system.mem_mode = 'timing'

# CPU Setup
system.cpu = X86O3CPU()

# exploration 2
# system.cpu.branchPred = LocalBP(localPredictorSize=2048, localCtrBits=2)

# change size of the tage BP
system.cpu.branchPred = TAGE()

## This is needed when we use x86 CPUs
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# L1 data cache setup
system.cpu.l1d = L1DCache()
system.cpu.l1d.cpu_side = system.cpu.dcache_port

# L1 instruction cache
system.cpu.l1i = L1ICache()
system.cpu.l1i.cpu_side = system.cpu.icache_port

# L2 cache setup
system.l2_cache = L2Cache()
system.l2_bus = L2XBar()

# l1 d
system.cpu.l1d.mem_side = system.l2_bus.cpu_side_ports

# exploration 1 will test the following
# system.cpu.l1d.prefetcher = StridePrefetcher()
# system.cpu.l1i.prefetcher = TaggedPrefetcher(degree=2)

# l1 i
system.cpu.l1i.mem_side = system.l2_bus.cpu_side_ports


# l2
system.l2_cache.mem_side = system.membus.cpu_side_ports
system.l2_cache.cpu_side = system.l2_bus.mem_side_ports

# Memory setup
system.mem_ctrl = MemCtrl()
system.mem_ctrl.port = system.membus.mem_side_ports

## A memory controller interfaces with main memory; create it here
system.mem_ctrl.dram = DDR3_1600_8x8()

## A DDR3_1600_8x8 has 8GB of memory, so setup an 8 GB address range
address_ranges = [AddrRange('8GB')]
system.mem_ranges = address_ranges
system.mem_ctrl.dram.range = address_ranges[0]

# Process setup
process = Process()

## Set up binary
binary = args.binary
if args.outFile:
   process.cmd = [binary, f'-o {args.outFile}', f'{args.inFile}']
else:
    process.cmd = [binary, f'{args.inFile}']

# Pass full command to init_compatible()
system.workload = SEWorkload.init_compatible(binary)

system.cpu.workload = process
system.cpu.createThreads()

# Start the simulation
root = Root(full_system=False, system=system) # must assign a root

m5.instantiate() # must be called before m5.simulate
m5.simulate()
