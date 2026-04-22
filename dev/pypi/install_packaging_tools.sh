#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/install_packaging_tools.sh
# Part of 'UBDCC Dashboard'
# License: MIT
# https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE

set -xeuo pipefail

python3 -m pip install --upgrade pip setuptools wheel twine build tqdm
