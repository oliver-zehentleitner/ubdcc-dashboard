#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/create_wheel.sh
# Part of 'UBDCC Dashboard'
# License: MIT
# https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE

set -euo pipefail

security_check() {
    echo -n "Did you bump the version in CHANGELOG.md and run 'python3 dev/set_version.py <new>'? [yes|NO] "
    read -r SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
}

compile() {
    echo "ok, lets go ..."
    python3 -m build --sdist --wheel
}

security_check
compile
