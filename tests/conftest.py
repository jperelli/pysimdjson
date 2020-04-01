import pytest


@pytest.fixture
def parser():
    import csimdjson
    yield csimdjson.parser()
