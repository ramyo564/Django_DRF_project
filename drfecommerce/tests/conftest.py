import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (

    CategoryFactory,
    ProductFactory,
    ProductLineFactory,
    ProductImageFactory,
    ProductLineAttributeValueFactory,
    ProductTypeFactory,
    AttributeFactory,
    AttributeValueFactory,

)

register(CategoryFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
register(ProductTypeFactory)
register(AttributeValueFactory)
register(AttributeFactory)
register(ProductLineAttributeValueFactory)

@pytest.fixture
def api_client():
    return APIClient
