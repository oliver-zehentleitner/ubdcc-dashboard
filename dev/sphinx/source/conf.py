# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../../..'))

# -- Project information -----------------------------------------------------

project = 'ubdcc-dashboard'
copyright = '2026, Oliver Zehentleitner'
author = 'Oliver Zehentleitner'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '0.3.0'

html_last_updated_fmt = "%b %d %Y at %H:%M (CET)"

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'
language = "en"
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = None

# -- Options for HTML output -------------------------------------------------

html_theme = 'python_docs_theme_ubs'
html_context = {'github_user_name': 'oliver-zehentleitner',
                'github_repo_name': 'ubdcc-dashboard',
                'project_name': project,
                'lucit': False}

myst_heading_anchors = 3

html_static_path = ['_static']

htmlhelp_basename = 'ubdcc-dashboard-apidoc'

latex_documents = [
    (master_doc, 'ubdcc-dashboard.tex',
     'ubdcc-dashboard Documentation',
     'Oliver Zehentleitner', 'manual'),
]

man_pages = [
    (master_doc, 'ubdcc-dashboard', 'ubdcc-dashboard Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'ubdcc-dashboard', 'ubdcc-dashboard Documentation',
     author, 'ubdcc-dashboard', 'Live dashboard for the UNICORN Binance DepthCache Cluster.',
     'Miscellaneous'),
]

epub_title = project
epub_exclude_files = ['search.docs']
