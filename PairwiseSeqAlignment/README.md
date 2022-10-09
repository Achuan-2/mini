

## Using Python to implement Needleman Wunsch and Smith Waterman algorithms

## Introduction

[Yuque Blog](https://www.yuque.com/achuan-2/blog/tfte2w)


## Install 
```shell
$ pip install PairwiseSeqAlignment
```
## Help
```shell
Usage: PairwiseSeqAlignment [OPTIONS]  

  Using Python to implement Needleman Wunsch and Smith Waterman algorithms
  for pairwise sequence alignment

Options:
  -1, --seq1 TEXT        The first sequence.
  -2, --seq2 TEXT        The second sequence.
  -m, --match FLOAT      The match score.
  -d, --mismatch FLOAT   The mismatch penalty.
  -g, --gap FLOAT        The gap open penalty.
  -e, --extension FLOAT  The gap extension penalty.
  -o, --output TEXT      The output directory.
  -G, --global           Choose Global alignment.[Default]
  -L, --local            Choose Local alignment.
  --help                 Show this message and exit.
```

