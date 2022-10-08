from setuptools import setup

setup(
    name='PairwiseSeqAlignment',
    version='0.1',
    py_modules=['PairwiseSeqAlignment'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        PairwiseSeqAlignment=main:main
    ''',
)
