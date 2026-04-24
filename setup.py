#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of 'UBDCC Dashboard'
# Project website: https://github.com/oliver-zehentleitner/ubdcc-dashboard
# Github: https://github.com/oliver-zehentleitner/ubdcc-dashboard
# Documentation: https://oliver-zehentleitner.github.io/ubdcc-dashboard
# PyPI: https://pypi.org/project/ubdcc-dashboard
#
# License: MIT
# https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE
#
# Author: Oliver Zehentleitner
#
# Copyright (c) 2026, Oliver Zehentleitner (https://about.me/oliver-zehentleitner)
# All rights reserved.

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ubdcc-dashboard",
    version="0.2.0",
    author="Oliver Zehentleitner",
    author_email="",
    url="https://github.com/oliver-zehentleitner/ubdcc-dashboard",
    description="Browser-based live dashboard for the UNICORN Binance DepthCache Cluster (UBDCC).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=[],
    python_requires=">=3.9.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    package_data={"ubdcc_dashboard": ["static/*.html", "static/*.css", "static/*.js"]},
    entry_points={
        "console_scripts": [
            "ubdcc-dashboard=ubdcc_dashboard.cli:main",
        ],
    },
    project_urls={
        "Howto": "https://github.com/oliver-zehentleitner/ubdcc-dashboard#howto",
        "Documentation": "https://oliver-zehentleitner.github.io/ubdcc-dashboard",
        "Wiki": "https://github.com/oliver-zehentleitner/ubdcc-dashboard/wiki",
        "Author": "https://www.linkedin.com/in/oliver-zehentleitner",
        "Changes": "https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/CHANGELOG.md",
        "License": "https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE",
        "Issue Tracker": "https://github.com/oliver-zehentleitner/ubdcc-dashboard/issues",
        "Telegram": "https://t.me/unicorndevs",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "Environment :: Web Environment",
    ],
    keywords="binance depthcache dashboard ubdcc unicorn monitoring",
)
