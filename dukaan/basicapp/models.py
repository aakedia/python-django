from django.db import models


# Category model having category_id as primary key
#  & {name, is_leaf, is_active, parent} as additional fields
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)

    name = models.TextField(max_length=1000, null=False, blank=False)

    is_leaf = models.BooleanField()

    is_active = models.BooleanField(default=True)

    parent = models.IntegerField(default=0)

    class Meta:
        db_table = 'Category'

    # def __str__(self):
    #     return self.name


# Product model having product_id as primary key
# & {name, description, is_active} as additional fields
# & category field is a foreign key referencing Category table
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)

    name = models.TextField(max_length=1000, null=False, blank=False)

    description = models.TextField(max_length=1000, null=False, blank=False)

    is_active = models.BooleanField(default=True)

    # on_delete CASCADE ensures that all the child entries are also deleted
    category = models.ForeignKey('Category', on_delete=models.CASCADE, )

    class Meta:
        db_table = 'Product'


# ProductVariations model having product_v_id as primary key
# & {colour, product_size, quantity, original_price,selling_price } as additional fields
# & product field is a foreign key referencing Product table
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
