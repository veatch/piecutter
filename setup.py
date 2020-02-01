#!/usr/bin/env python

from setuptools import setup

requirements = [
    "cookiecutter<2"
]

extras_require = dict(
    test=[
        'pytest',
    ]
)


setup(
    name="piecutter",
    author="Jason Veatch",
    url="https://github.com/veatch/piecutter",
    entry_points={
        'console_scripts': [
            'piecutter = piecutter.__main__:main',
        ]
    },
    install_requires=requirements,
    extras_require=extras_require
)
