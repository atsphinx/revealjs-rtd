"""Config of demo."""

import os

from atsphinx.revealjs_rtd import __version__

project = "atsphinx-revealjs-rtd"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = [
    "rst_budoux.sphinx",
    "atsphinx.mini18n",
    "atsphinx.revealjs_rtd",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "ja"

# -- Options for Revealjs output
revealjs_html_theme = "revealjs-simple"
revealjs_static_path = ["_static"]
revealjs_style_theme = "black"
revealjs_script_conf = {
    "controls": False,
    "progress": True,
    "hash": True,
    "center": True,
    "transition": "slide",
}
revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealMath",
        "src": "revealjs/plugin/math/math.js",
    },
]
revealjs_css_files = [
    "revealjs/plugin/highlight/zenburn.css",
]
revealjs_notes_from_comments = True

# -- Options for extensions
# rst_budoux.sphinx
budoux_separator = "<wbr>"
budoux_additional_style = """
body {
    word-break: keep-all;
    overflow-wrap: anywhere;
}
"""
# atsphinx-mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_basepath = ""
if "READTHEDOCS_VERSION" in os.environ:
    mini18n_basepath = f"/{os.environ['READTHEDOCS_VERSION']}/"
