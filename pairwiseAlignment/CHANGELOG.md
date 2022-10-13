## 2022.10.13
- :art: reorganization the project
- :bug: 修正全局比对第一个cell是0的情况


## 2022.10.09
- 添加了mkdir函数功能，以及--ouput参数
- 运行完成终端会打印align结果
- 完善Commandline模块，支持选择全局比对或局部比对
- 上传到Pypi https://pypi.org/project/pairwiseAlignment/
## 2022.10.08
- 修复了调用plot_align时，参数重复出现的情况
- 学习了python面向对象的@property魔术方法，就给对象的parameters、align_results、scoremat、tracemat加了
- 添加Click模块，支持Commandline
- 支持penalty输入float number

## 2022.10.07

* 修复了代码里的一些小bug，比如局部比对的回溯应该是score等于0，我写成trace等于0了……
* 添加了打印参数内容
* 添加了打印score分数，score分数就是traceback的起始点的分值！