from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('product/list/grid/', views.ShopProductGridListView.as_view(), name='list_grid'),
    path('product/list/', views.ShopProductListView.as_view(), name='list'),
    path('product/<slug>/detail/', views.ShopProductDetailView.as_view(), name='detail'),
]
