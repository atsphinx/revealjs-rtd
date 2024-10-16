"""Config of demo."""

from atsphinx.revealjs_rtd import __version__

project = "atsphinx-revealjs-rtd"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = [
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
