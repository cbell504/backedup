#!usr/bin/env python3

from setuptools import setup

setup(
    name='backup',
    version='1.0.0',
    description='simple backup script',
    author='Azurras',
    url='https://github.com/Azurras/backup.git',
    author_email='',
    keyword=['backup'],
    entry_pints={'console_scripts': [
        'backup = backup.__main__:main',
    ],},
)