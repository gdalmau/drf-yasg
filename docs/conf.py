#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# drf_yasg2 documentation build configuration file, created by
# sphinx-quickstart on Sun Dec 10 15:20:34 2017.
import inspect
import os
import re
import sys

import sphinx_rtd_theme
from docutils import nodes, utils
from docutils.parsers.rst import roles
from docutils.parsers.rst.roles import set_classes
from pkg_resources import get_distribution

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

version = "1.18.0"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "drf_yasg2"
copyright = "2020, Joel Lefkowitz"
author = "Joel Lefkowitz"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

modindex_common_prefix = ["drf_yasg2."]

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'default'

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    "**": [
        "relations.html",  # needs 'show_related': True theme option to display
        "searchbox.html",
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "drf_yasg2doc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "drf_yasg2.tex", "drf_yasg2 Documentation", "Joel Lefkowitz", "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "drf_yasg2", "drf_yasg2 Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "drf_yasg2",
        "drf_yasg2 Documentation",
        author,
        "drf_yasg2",
        "One line description of project.",
        "Miscellaneous",
    ),
]

autodoc_default_options = {"private-members": None}
autodoc_member_order = "bysource"
autoclass_content = "both"
autodoc_mock_imports = []

nitpick_ignore = [
    ("py:class", "object"),
    ("py:class", "bool"),
    ("py:class", "dict"),
    ("py:class", "list"),
    ("py:class", "str"),
    ("py:class", "int"),
    ("py:class", "bytes"),
    ("py:class", "tuple"),
    ("py:class", "function"),
    ("py:class", "type"),
    ("py:class", "OrderedDict"),
    ("py:class", "None"),
    ("py:obj", "None"),
    ("py:class", "Exception"),
    ("py:class", "collections.OrderedDict"),
    ("py:class", "ruamel.yaml.dumper.SafeDumper"),
    ("py:class", "rest_framework.serializers.Serializer"),
    ("py:class", "rest_framework.renderers.BaseRenderer"),
    ("py:class", "rest_framework.parsers.BaseParser"),
    ("py:class", "rest_framework.schemas.generators.EndpointEnumerator"),
    ("py:class", "rest_framework.views.APIView"),
    ("py:class", "OpenAPICodecYaml"),
    ("py:class", "OpenAPICodecJson"),
    ("py:class", "OpenAPISchemaGenerator"),
    ("py:class", "coreapi.Field"),
    ("py:class", "BaseFilterBackend"),
    ("py:class", "BasePagination"),
    ("py:class", "Request"),
    ("py:class", "rest_framework.request.Request"),
    ("py:class", "rest_framework.serializers.Field"),
    ("py:class", "serializers.Field"),
    ("py:class", "serializers.BaseSerializer"),
    ("py:class", "Serializer"),
    ("py:class", "BaseSerializer"),
    ("py:class", "APIView"),
]

# even though the package should be already installed, the sphinx build on RTD
# for some reason needs the sources dir to be in the path in order for viewcode to work
sys.path.insert(0, os.path.abspath("../src"))

# activate the Django testproj to be able to succesfully import drf_yasg
sys.path.insert(0, os.path.abspath("../testproj"))
os.putenv("DJANGO_SETTINGS_MODULE", "testproj.settings.local")

from django.conf import settings  # noqa: E402

settings.configure()

# instantiate a SchemaView in the views module to make it available to autodoc
import drf_yasg2.views  # noqa: E402

drf_yasg2.views.SchemaView = drf_yasg2.views.get_schema_view(None)

# monkey patch to stop sphinx from trying to find classes by their real location instead of the
# top-level __init__ alias; this allows us to document only `drf_yasg2.inspectors` and avoid 
# broken references or double documenting

import drf_yasg2.inspectors  # noqa: E402


def redirect_cls(cls):
    if cls.__module__.startswith("drf_yasg2.inspectors"):
        return getattr(drf_yasg2.inspectors, cls.__name__)
    return cls


for cls_name in drf_yasg2.inspectors.__all__:

    # first pass - replace all classes' module with the top level module
    real_cls = getattr(drf_yasg2.inspectors, cls_name)
    if not inspect.isclass(real_cls):
        continue

    patched_dict = dict(real_cls.__dict__)
    patched_dict.update({"__module__": "drf_yasg2.inspectors"})
    patched_cls = type(cls_name, real_cls.__bases__, patched_dict)
    setattr(drf_yasg2.inspectors, cls_name, patched_cls)

for cls_name in drf_yasg2.inspectors.__all__:

    # second pass - replace the inheritance bases for all classes to point to the new clean classes
    real_cls = getattr(drf_yasg2.inspectors, cls_name)
    if not inspect.isclass(real_cls):
        continue

    patched_bases = tuple(redirect_cls(base) for base in real_cls.__bases__)
    patched_cls = type(cls_name, patched_bases, dict(real_cls.__dict__))
    setattr(drf_yasg2.inspectors, cls_name, patched_cls)

# custom interpreted role for linking to GitHub issues and pull requests
# use as :issue:`14` or :pr:`17`
gh_issue_uri = "https://github.com/axnsan12/drf_yasg2/issues/{}"
gh_pr_uri = "https://github.com/axnsan12/drf_yasg2/pull/{}"
gh_user_uri = "https://github.com/{}"


def sphinx_err(inliner, lineno, rawtext, msg):
    msg = inliner.reporter.error(msg, line=lineno)
    prb = inliner.problematic(rawtext, rawtext, msg)
    return [prb], [msg]


def sphinx_ref(options, rawtext, text, ref):
    set_classes(options)
    node = nodes.reference(rawtext, text, refuri=ref, **options)
    return [node], []


def role_github_user(name, rawtext, text, lineno, inliner, options=None, content=None):
    options = options or {}
    content = content or []

    if not re.match(r"^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$", text, re.IGNORECASE):
        return sphinx_err(
            inliner, lineno, rawtext, '"%s" is not a valid GitHub username.' % text
        )

    ref = gh_user_uri.format(text)
    text = "@" + utils.unescape(text)
    return sphinx_ref(options, rawtext, text, ref)


def role_github_pull_request_or_issue(
    name, rawtext, text, lineno, inliner, options=None, content=None
):
    options = options or {}
    content = content or []
    try:
        if int(text) <= 0:
            raise ValueError
    except ValueError:
        return sphinx_err(
            inliner,
            lineno,
            rawtext,
            'GitHub pull request or issue number must be a number greater than or equal to 1; "%s" is invalid.'
            % text,
        )

    if name == "pr":
        ref = gh_pr_uri
    elif name == "issue":
        ref = gh_issue_uri
    else:
        return sphinx_err(
            inliner,
            lineno,
            rawtext,
            'unknown role name for GitHub reference - "%s"' % name,
        )

    ref = ref.format(text)
    text = "#" + utils.unescape(text)
    return sphinx_ref(options, rawtext, text, ref)


roles.register_local_role("pr", role_github_pull_request_or_issue)
roles.register_local_role("issue", role_github_pull_request_or_issue)
roles.register_local_role("ghuser", role_github_user)


def setup(app):
    app.add_css_file("css/style.css")
