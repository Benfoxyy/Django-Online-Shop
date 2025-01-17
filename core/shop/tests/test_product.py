import pytest


@pytest.mark.django_db
def test_product(create_product):
    # Test user email
    assert create_product.user.email == "test@gmail.com"

    # Test categories (ManyToManyField requires iteration)
    categories = create_product.category.all()
    assert len(categories) == 1  # Ensure there's one category
    assert categories[0].title == "test"  # Check the title of the category

    # Test product attributes
    assert create_product.title == "test"
    assert create_product.slug == "test"
    assert create_product.description == "test"
    assert create_product.price == 1000
    assert create_product.discount_percent == 0
    assert create_product.avg_rate == 0.0

    # Test methods
    assert create_product.is_published()
    assert create_product.offer() == 1000
