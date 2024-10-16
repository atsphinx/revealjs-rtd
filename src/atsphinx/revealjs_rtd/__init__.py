"""Optimize for sphinx-revealjs on Read the Docs."""

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.config import Config

__version__ = "0.0.0"

root = Path(__file__).parent


def append_settings(app: Sphinx, config: Config):
    """Configure settinfs for sphinx-revealjs."""
    config.revealjs_static_path.append(str(root / "static"))
    config.revealjs_script_plugins.append(
        {
            "name": "RevealRTD",
            "src": "atsphinx-revealjs-rtd/rtd.js",
        }
    )


def setup(app: Sphinx):  # noqa: D103
    app.setup_extension("sphinx_revealjs")
    app.connect("config-inited", append_settings)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
