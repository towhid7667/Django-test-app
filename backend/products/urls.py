from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_create_view, name='product-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update', views.product_update_view),
    path('<int:pk>/delete', views.product_destroy_view)

]