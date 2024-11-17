from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('checkout/',views.CheckOutView.as_view(),name='checkout'),
    path('complete/',views.OrderCompleteView.as_view(),name='complete'),
]
