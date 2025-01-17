import pytest
from shop.models import CategoryModel, ProductModel
from accounts.models import User


@pytest.fixture
def create_user():
    return User.objects.create_user(
        email="test@gmail.com", password="ben_ya_min"
    )


@pytest.fixture
def create_category():
    return CategoryModel.objects.create(title="test", slug="test")


@pytest.fixture
def create_product(create_user, create_category):
    product = ProductModel.objects.create(
        user=create_user,
        title="test",
        slug="test",
        description="test",
        price=1000,
    )
    # Assign the category using the `.set()` method
    product.category.set([create_category])
    return product
