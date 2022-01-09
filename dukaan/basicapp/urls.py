from django.urls import path
from .views import CategoryView, ProductView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:id>/', CategoryView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<int:id>/', ProductView.as_view()),
]