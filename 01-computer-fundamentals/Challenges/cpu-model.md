# Challenge: Find Your CPU Model

## Objective

Identify the exact CPU model and number of CPU cores.

## Tool Used

`lscpu`

## Results

- **CPU:** AMD Ryzen 5 5600 6-Core Processor
- **Cores:** 6
- **Threads per core:** 2
- **Logical CPUs:** 12
- **Architecture:** x86_64
- **Virtualization:** AMD-V

## What I Learned

I used `lscpu` to inspect detailed CPU information.

My CPU has 6 physical cores and 12 logical CPUs because it has 2 threads per core.

The `lscpu` output also provides information about the CPU architecture, virtualization, caches, and security-related CPU vulnerability mitigations.

## Command

```bash
lscpu