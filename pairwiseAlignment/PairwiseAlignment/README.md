

## Using Python to implement Needleman Wunsch and Smith Waterman algorithms

## Introduction

[Yuque Blog](https://www.yuque.com/achuan-2/blog/tfte2w)


## Install 
```shell
$ pip install pairwiseAlignment
```
## Help
```
Usage: pairwiseAlignment [OPTIONS]  

  Using Python to implement Needleman Wunsch and Smith Waterman algorithms
  for pairwise sequence alignment

Options:
  -1, --seq1 TEXT        The first sequence.
  -2, --seq2 TEXT        The second sequence.
  -m, --match FLOAT      The match score.  [default: 1.0]
  -d, --mismatch FLOAT   The mismatch penalty.  [default: -1.0]
  -g, --gap FLOAT        The gap open penalty.  [default: -2.0]
  -e, --extension FLOAT  The gap extension penalty.  [default: -1.0]
  -o, --output TEXT      The output directory.  [default: output]
  -G, --global           Choose global alignment.[default]
  -L, --local            Choose local alignment.
  -n, --nosave           Do not save the alignment result.
  --help                 Show this message and exit
```

