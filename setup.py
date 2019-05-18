# -*- coding: utf-8 -*-

import re
from setuptools import setup
 
 
version = re.search(
    r'^__version__\s*=\s*"(.*)"',
    open('scyence/scyence.py').read(),
    re.M
    ).group(1)
 
with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name='scyence',
    packages=['scyence'],
    entry_points = {
        "console_scripts": ['scyence = scyence.__main__:main']
        },
    include_package_data=True,
    install_requires=[''],
    version = version,
    description='scyence - scientific and mathematic utilities',
    long_description = long_descr,
    author='zzara',
    author_email='zzara@protonmail.com',
    )
