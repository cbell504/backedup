#!usr/bin/env python3

from setuptools import setup

setup(
    name='backupper',
    packages=['backupper'],
    package_dir={'backupper': 'backupper'},
    version='1.0.0',
    description='simple backup script',
    author='Azurras',
    url='https://github.com/Azurras/backup.git',
    author_email='',
    keywords=['backup'],
    entry_points={'console_scripts': [
        'backupper = backupper.__main__:main',
    ], },
)
