import pytest


@pytest.mark.django_db
def test_user(create_user):
    assert create_user.email == "test@gmail.com"
