import pytest


@pytest.fixture
def cpfs_validos():
    return [
        "52998224725",
        "16899535009",
        "11144477735",
    ]


@pytest.fixture
def cpfs_invalidos():
    return [
        "52998224724",
        "11111111111",
        "123456789",
        "123456789012",
        "abc12345678",
        "",
        None,
    ]