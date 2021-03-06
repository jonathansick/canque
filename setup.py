#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup


setup(
    name="canque",
    version="0.1",
    packages=["canque"],
    install_requires=['Jinja2'],
    author="Jonathan Sick",
    author_email="jonathansick@mac.com",
    description="Make CANFAR queue submission files.",
    license="BSD",
    keywords="astronomy",
    url="http://github.com/jonathansick/canque",
)
