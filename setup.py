#!/usr/bin/env python
from setuptools import setup

requires = []

entry_points = {
    'console_scripts': []
}

packages = []

setup(
    name='pelican-tools',
    version='1.0.0',
    url='http://getpelican.com/',
    author='Alexis Metaireau',
    author_email='authors@getpelican.com',
    description='Tools developed for the Pelican static site generator.',
    long_description=open('README.md').read(),
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
