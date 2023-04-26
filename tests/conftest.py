import pytest


DICT = {"vcs": "mercurial", "num": 275, "float_num": 23.56}


@pytest.fixture
def dict_fixture():
    return DICT
