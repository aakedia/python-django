from django.db import models


# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)

    name = models.TextField(max_length=1000, null=False, blank=False)

    is_leaf = models.BooleanField()

    is_active = models.BooleanField(default=True)

    parent = models.IntegerField(default=0)

    class Meta:
        db_table = 'Category'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)

    name = models.TextField(max_length=1000, null=False, blank=False)

    description = models.TextField(max_length=1000, null=False, blank=False)

    is_active = models.BooleanField(default=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, )

    class Meta:
        db_table = 'Product'


class ProductVariations(models.Model):
    product_v_id = models.AutoField(primary_key=True)

    colour = models.TextField(max_length=1000, )

    product_size = models.TextField(max_length=1000, )

    quantity = models.PositiveIntegerField(default=1)

    original_price = models.FloatField(default=1)

    selling_price = models.FloatField(default=1)

    product = models.ForeignKey('Product', on_delete=models.CASCADE, )

    class Meta:
        db_table = 'Product_Variations'
