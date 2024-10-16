"""Standard tests."""

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs")
def test__it(app: SphinxTestApp):
    """Test to pass."""
    app.build()
