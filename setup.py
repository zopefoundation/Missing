##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import find_packages
from setuptools import setup


README = open('README.rst').read()
CHANGES = open('CHANGES.rst').read()

version = '5.1.dev0'

setup(
    name='Missing',
    version=version,
    url='https://github.com/zopefoundation/Missing',
    project_urls={
        'Issue Tracker': 'https://github.com/zopefoundation/Missing/issues',
        'Sources': 'https://github.com/zopefoundation/Missing',
    },
    license='ZPL-2.1',
    description="Special Missing objects used in Zope.",
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    long_description='\n\n'.join([README, CHANGES]),
    keywords="zope missing object",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires='>=3.9',
    install_requires=[
        'ExtensionClass >= 4.1a1',
        'zope.deferredimport',
    ],
    include_package_data=True,
    zip_safe=False,
)
