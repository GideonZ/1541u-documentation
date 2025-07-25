# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Ultimate Documentation'
copyright = '2025, Gideon Zweijtzer'
author = 'Gideon Zweijtzer'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#import guzzle_sphinx_theme

#html_theme_path = guzzle_sphinx_theme.html_theme_path()
#html_theme = 'guzzle_sphinx_theme'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_local']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

def setup(app):
    if hasattr(app, 'add_css_file'):
        app.add_css_file('theme_overrides.css')  # Older sphinx
    else:
        app.add_stylesheet('theme_overrides.css')  # Newer sphinx

#html_context = {
#    'css_files': [
#        '_static/theme_overrides.css',  # override wide tables in RTD theme
#        ],
#     }
