from django.urls import path
from . import views
urlpatterns = [
    path('product', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('category', views.CatagoryList.as_view()),
    path('category/<int:pk>/', views.CatagoryDetail.as_view()),
    path('manufacturer', views.manufacturerList.as_view()),
    path('manufacturer/<int:pk>/', views.manufacturerDetail.as_view()),
]
