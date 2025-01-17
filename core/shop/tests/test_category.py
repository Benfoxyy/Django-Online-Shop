import pytest


@pytest.mark.django_db
def test_product_category(create_category):
    assert create_category.title == "test"
    assert create_category.slug == "test"
