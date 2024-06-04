from django.urls import path

from . import views
from .views import ProductListView, CommentCreateView

urlpatterns = [

    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),


]
