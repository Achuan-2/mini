from setuptools import setup

setup(
    name='seqAlignment',
    version='0.1',
    py_modules=['seqAlignment'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        seqAlignment=main:main
    ''',
)
