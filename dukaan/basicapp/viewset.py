from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from . import models
from . import serializers


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def create(self, request, *args, **kwargs):
        category_data = request.data
        new_category = models.Category.objects.create(name=category_data["name"], is_leaf=category_data["is_leaf"],
                                                      is_active=category_data["is_active"],
                                                      parent=category_data["parent"])
        new_category.save()
        if category_data["parent"] != '0':
            queryset = models.Category.objects.get(category_id=category_data["parent"])
            queryset.is_leaf = False
            queryset.save()
        return Response(serializers.CategorySerializer.data)

    @action(detail=False, url_path=r'children/(?P<category>\w+)', methods=['get'])
    def children(self, request, *args, **kwargs):
        # queryset = models.Category.objects.all()
        # print(queryset)
        #
        # serializer = serializers.CategorySerializer(queryset, many=True).data
        #
        # q = deque()
        # q.append(serializer.get(category_id = self.kwargs['category']))
        # print(q)
        # print(serializer)
        return Response()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductVariationsViewSet(viewsets.ModelViewSet):
    queryset = models.ProductVariations.objects.all()
    serializer_class = serializers.ProductVariationsSerializer

    @action(detail=False, url_path=r'variations/(?P<product>\w+)', methods=['get'])
    def variations(self, request, *args, **kwargs):
        queryset = models.ProductVariations.objects.filter(product=self.kwargs['product'])
        serializer = serializers.ProductVariationsSerializer(queryset, many=True).data
        print(serializer)
        return Response(serializer)
