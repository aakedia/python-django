from django.urls import path, include
from rest_framework import routers

from basicapp.viewset import CategoryViewSet
from basicapp.viewset import ProductViewSet
from basicapp.viewset import ProductVariationsViewSet

# Auto generates the urls for a particular viewset
router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("product", ProductViewSet)
router.register("productvar", ProductVariationsViewSet)