from utils import dicts


def test__get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, None, "git") == "git"
    assert dicts.get_val({}, "vcs", "git") == "git"
