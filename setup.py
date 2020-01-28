#!usr/bin/env python3

from setuptools import setup

setup(
    name='backedup',
    packages=['backedup'],
    package_dir={'backedup': 'backedup'},
    version='1.0.0',
    description='A simple backup script',
    author='Azurras',
    url='https://github.com/Azurras/backedup.git',
    author_email='',
    keywords=['backedup'],
    entry_points={'console_scripts': [
        'backedup = backedup.__main__:main',
    ], },
)
