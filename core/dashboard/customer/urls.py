from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('home/',views.CustomerDashboard.as_view(),name='home'),
    path('change-pass/',views.ChangePassView.as_view(),name='change-pass'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('addresses/',views.AddressesView.as_view(),name='addresses'),
    path('addresses-add/',views.AddAddressesView.as_view(),name='add-addresses'),
    path('addresses-change/<int:pk>/',views.ChangeAddressesView.as_view(),name='change-addresses'),
    path('orders/',views.OrderView.as_view(),name='orders'),
    path('order/<int:pk>/',views.OrderDetailView.as_view(),name='order-detail'),
    path('order/<int:pk>/invoice/',views.OrderInvoiceView.as_view(),name='order-invoice'),
    path('whishlist/',views.WishListView.as_view(),name='wishlist'),
    path('whishlist/delete/<int:pk>/',views.DeleteWishView.as_view(),name='delete-wish'),
]
