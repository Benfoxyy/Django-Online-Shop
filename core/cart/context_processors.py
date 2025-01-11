from .cart import CartSession


def CartProcessor(request):
    cart = CartSession(request.session)
    return {"cart": cart}
