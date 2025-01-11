from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .cart import CartSession


@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    cart = CartSession(request.session)
    cart.cart_sync(user=user)


@receiver(user_logged_out)
def pre_logout(sender, user, request, **kwargs):
    cart = CartSession(request.session)
    cart.cart_merge(user=user)
