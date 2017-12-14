#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "firefox-tabs",
    description = "A library and cli app for accessing your open Firefox tabs.",
    author = "Erik Wickstrom",
    author_email = "erik@erikwickstrom.com",
    url = "https://github.com/erikcw/firefox-tabs",
    version = "0.1",
    packages = find_packages(),
    zip_safe = False,
    include_package_data=True,
    install_requires=['lz4',],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
