# from django.test import TestCase
# from .models import Category, Product, ProductVariations
#
#
# # models test
# class CategoryTest(TestCase):
#
#     def create_category(self, name="only a test", is_leaf=True, is_active=True, parent=1):
#         return Category.objects.create(name=name, is_leaf=is_leaf, is_active=is_active, parent=parent)
#
#     def test_create_category(self):
#         c = self.create_category()
#         self.assertTrue(isinstance(c, Category))
#         self.assertEqual(str(c), c.name)
