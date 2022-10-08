

使用Python实现Needleman-Wunsch和Smith-Waterman算法 with affine gap scores
# Algorithm
| 性质     | Smith-Waterman              | Needleman-Wunsch    |
| ---------- | ----------------------------- | ----------------------- |
| 初始化   | 行列全部置0                 | 第0行和第0列置GAP罚分 |
| 得分方式 | 负分置0                     | 允许负分              |
| 回溯方式 | 最高分开始->位点分数为0结束 | 右下角->左上角        |
![20221008233206](https://cdn.jsdelivr.net/gh/Achuan-2/PicBed@pic/assets/README/20221008233206.png)
![20221008233134](https://cdn.jsdelivr.net/gh/Achuan-2/PicBed@pic/assets/README/20221008233134.png)
## Install 
```shell
$ pip install --editable .
```
## Help
```shell
Usage: seqAlignment [OPTIONS]

Options:
  -1, --seq1 TEXT          The first sequence.
  -2, --seq2 TEXT          The second sequence.
  -m, --match INTEGER      The match score.
  -d, --mismatch INTEGER   The mismatch score.
  -g, --gap INTEGER        The gap score.
  -e, --extension INTEGER  The extension score.
  --help                   Show this message and exit.
```