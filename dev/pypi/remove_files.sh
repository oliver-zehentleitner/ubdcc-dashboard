#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/remove_files.sh
# Part of 'UBDCC Dashboard'
# License: MIT
# https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE

set -xuo

rm -rf ./build
rm -rf ./dist
rm -rf ./*.egg-info
