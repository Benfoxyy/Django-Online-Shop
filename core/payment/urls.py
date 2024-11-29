from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('verify',views.VerificationView.as_view(),name='cart-summery'),
]