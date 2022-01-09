from rest_framework import routers

from basicapp.viewset import CategoryViewSet
from basicapp.viewset import ProductViewSet
from basicapp.viewset import ProductVariationsViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("product", ProductViewSet)
router.register("productvar", ProductVariationsViewSet)
