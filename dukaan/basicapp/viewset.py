from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from . import models
from . import serializers


# Category view, to expose GET, POST, PUT, DELETE methods on Category model
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    # Override def create method so that if a child category is introduced
    # then the is_leaf field of parent category automatically gets updated.
    def create(self, request, *args, **kwargs):
        category_data = request.data
        new_category = models.Category.objects.create(name=category_data["name"], is_leaf=category_data["is_leaf"],
                                                      is_active=category_data["is_active"],
                                                      parent=category_data["parent"])
        new_category.save()
        # Check to see if the field added is root field
        if category_data["parent"] != '0':
            queryset = models.Category.objects.get(category_id=category_data["parent"])
            queryset.is_leaf = False
            queryset.save()
        return Response(serializers.CategorySerializer.data)

    # Exposed additional end point /children/<category-id> to retrieve the list of children of a category
    @action(detail=False, url_path=r'children/(?P<category>\w+)', methods=['get'])
    def children(self, request, *args, **kwargs):
        queryset = models.Category.objects.filter(parent=self.kwargs['category'])
        serializer = serializers.CategorySerializer(queryset, many=True).data
        print(serializer)
        return Response(serializer)


# Category view, to expose GET, POST, PUT, DELETE methods on Product model
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


# Category view, to expose GET, POST, PUT, DELETE methods on Product Variations model
class ProductVariationsViewSet(viewsets.ModelViewSet):
    queryset = models.ProductVariations.objects.all()
    serializer_class = serializers.ProductVariationsSerializer

    # Exposed additional end point /variations/<product-id> to retrieve the list of product variations associated
    # with a single product
    @action(detail=False, url_path=r'variations/(?P<product>\w+)', methods=['get'])
    def variations(self, request, *args, **kwargs):
        queryset = models.ProductVariations.objects.filter(product=self.kwargs['product'])
        serializer = serializers.ProductVariationsSerializer(queryset, many=True).data
        print(serializer)
        return Response(serializer)
