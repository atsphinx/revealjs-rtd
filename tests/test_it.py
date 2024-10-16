"""Standard tests."""

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs")
def test__it(app: SphinxTestApp):
    """Test to pass."""
    app.build()
    assert (app.outdir / "_static/atsphinx-revealjs-rtd/rtd.js").exists()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    scripts = [
        s
        for s in soup.find_all("script")
        if "src" in s.attrs and s["src"].endswith("atsphinx-revealjs-rtd/rtd.js")
    ]
    assert scripts
