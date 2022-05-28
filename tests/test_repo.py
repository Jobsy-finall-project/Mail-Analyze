import json

import pytest

from repo.tag_repo import add_tag
from repo.tag_repo import get_all


@pytest.fixture(autouse=True)
def cleanup():
    model = get_all()
    yield
    with open("repo/tag_pool.json", mode="w") as file:
        json.dump(model, file, indent=4)


def test_add_new_tag():
    add_tag("test")
    model = get_all()
    assert "test" in model


def test_add_duplicate():
    add_tag("Lingo")
    model = get_all()
    assert "Lingo" in model
