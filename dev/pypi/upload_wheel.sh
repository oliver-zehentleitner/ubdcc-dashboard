#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/upload_wheel.sh
# Part of 'UBDCC Dashboard'
# License: MIT
# https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE
#
# Requires a ~/.pypirc with valid API token.

set -xeuo pipefail

python3 -m twine upload dist/*
