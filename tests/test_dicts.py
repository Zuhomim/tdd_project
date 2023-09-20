from utils import dicts
import pytest


@pytest.fixture
def coll():
    return {"vcs": "mercurial"}


def test__get_val(coll):
    assert dicts.get_val(coll, "vcs", "git") == "mercurial"
    assert dicts.get_val(coll, None, "git") == "git"
    assert dicts.get_val({}, "vcs", "git") == "git"
