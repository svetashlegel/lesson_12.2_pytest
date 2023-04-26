from utils import dicts


def test_get_val(dict_fixture):
    assert dicts.get_val(dict_fixture, "vcs") == "mercurial"
    assert dicts.get_val(dict_fixture, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"
    assert dicts.get_val({}, "vcs", "bazar") == "bazar"
    assert dicts.get_val(dict_fixture, "bazar") == "git"
