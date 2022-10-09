from setuptools import setup,find_packages
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), 'r', encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
    install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

with open(path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PairwiseSeqAlignment',  # 必填，项目的名字，用户根据这个名字安装，pip install PairwiseSeqAlignment
    version='0.1.1', # 必填，项目的版本，建议遵循语义化版本规范
    author='Achuan-2',  # 项目的作者
    description='Using Python to implement Needleman Wunsch and Smith Waterman algorithms',  # 项目的一个简短描述
    long_description=long_description,  # 项目的详细说明，通常读取 README.md 文件的内容
    long_description_content_type='text/markdown',  # 描述的格式，可选的值： text/plain, text/x-rst, and text/markdown
    author_email='achuan-2@outlook.com',  # 作者的有效邮箱地址
    url='https://github.com/Achuan-2/mini/tree/main/PairwiseSeqAlignment',  # 项目的源码地址
    py_modules=['PairwiseSeqAlignment'],
    packages=find_packages(), # 项目的包列表，如果项目只有一个包，那么这个参数可以省略
    license='MIT', # 项目的许可证
    install_requires=install_requires,
    #  下面的设置将在命令行提供一个叫做 PairwiseSeqAlignment 的命令，用来执行 main.py 的 main 方法
    entry_points='''
        [console_scripts]
        PairwiseSeqAlignment=main:main
    ''',
)
