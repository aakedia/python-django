# tests/test_serializers.py
from django.test import TestCase

from .test_factory import CategoryFactory
from .serializers import CategorySerializer


# class CategorySerializer(TestCase):
#     def test_model_fields(self):
#         """Serializer data matches the Company object for each field."""
#         category = CategoryFactory()
#         for field_name in [
#             'id', 'name', 'description', 'website', 'street_line_1', 'street_line_2',
#             'city', 'state', 'zipcode'
#         ]:
#             self.assertEqual(
#                 serializer.data[field_name],
#                 getattr(category, field_name)
#             )