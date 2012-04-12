#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import potpie

install_requires = [
    "polib",
]

setup(
    name="potpie",
    version=potpie.__version__,
    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",
    url="https://github.com/dstufft/potpie",
    description="Translation Utility to Create Pseudo Translations of PO Files",
    long_description=open('README.rst').read(),
    license=open("LICENSE").read(),
    package_data={"": ["LICENSE"]},
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "potpie = potpie.__main__:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
