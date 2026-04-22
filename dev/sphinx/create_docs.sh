#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/sphinx/create_docs.sh
# Part of 'UBDCC Dashboard'
# License: MIT
# https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE

set -euo pipefail

rm -f dev/sphinx/source/changelog.md
rm -f dev/sphinx/source/code_of_conduct.md
rm -f dev/sphinx/source/contributing.md
rm -f dev/sphinx/source/readme.md
rm -f dev/sphinx/source/security.md

cp CHANGELOG.md dev/sphinx/source/changelog.md
cp CODE_OF_CONDUCT.md dev/sphinx/source/code_of_conduct.md
cp CONTRIBUTING.md dev/sphinx/source/contributing.md
cp README.md dev/sphinx/source/readme.md
cp SECURITY.md dev/sphinx/source/security.md

mkdir -p dev/sphinx/build

cd dev/sphinx
rm -f build/html
ln -sf ../../../docs build/html
make html -d
echo "Creating CNAME file for GitHub."
echo "oliver-zehentleitner.github.io" > build/html/CNAME
