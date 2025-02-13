import re
from shop.models import ProductModel, ProductStatus
from .models import CartModel, CartItemModel


class CartSession:
    def __init__(self, session):
        self.session = session
        self.cart = self.session.setdefault(
            "cart",
            {
                "items": [],
                "total_price": 0,
                "total_items": 0,
            },
        )

    def add_prod(self, product_id, quantity=None):
        for item in self.cart["items"]:
            if product_id == item["product_id"]:
                if quantity is None:
                    if (
                        ProductModel.objects.get(
                            id=product_id, status=ProductStatus.active.value
                        ).stock
                        > item["quantity"]
                    ):
                        item["quantity"] += 1
                    else:
                        return False
                else:
                    if ProductModel.objects.get(
                        id=product_id, status=ProductStatus.active.value
                    ).stock > item["quantity"] + int(quantity):
                        item["quantity"] += int(quantity)
                    else:
                        return False
                break
        else:
            new_prod = {
                "product_id": product_id,
                "quantity": 1 if quantity is None else int(quantity),
            }
            self.cart["items"].append(new_prod)
        self.save()

    def del_prod(self, product_id):
        for item in self.cart["items"]:
            if product_id == item["product_id"]:
                self.cart["items"].remove(item)
                break
        else:
            return
        self.save()

    def get_cart(self):
        return self.cart

    def get_cart_items(self):
        for item in self.cart["items"]:
            prod_obj = ProductModel.objects.get(
                id=item["product_id"], status=ProductStatus.active.value
            )
            item.update({"prod_obj": prod_obj})

        return self.cart["items"]

    def get_cart_quantity(self):
        return sum(int(item["quantity"]) for item in self.cart["items"])

    def get_total_price(self):
        items = self.get_cart_items()
        for item in items:
            if not item.get("prod_obj").discount_percent:
                self.cart["total_price"] += item.get("prod_obj").price * int(
                    item.get("quantity")
                )
            else:
                self.cart["total_price"] += item.get(
                    "prod_obj"
                ).offer() * int(item.get("quantity"))
        # tax = self.cart['total_price'] * Decimal('0.09')

        return self.cart["total_price"]

    def change_prod_quantity(self, product_id, quantity):
        for item in self.cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] = int(quantity)
                break
        else:
            return
        self.save()

    def clear(self):
        self.cart.update(
            {
                "items": [],
                "total_price": 0,
                "total_items": 0,
            }
        )

        self.save()

    def save(self):
        self.session.modified = True

    def cart_sync(self, user):
        cart_model, created = CartModel.objects.get_or_create(user=user)
        cart_items = CartItemModel.objects.filter(cart=cart_model)
        for cart_item in cart_items:
            for item in self.cart["items"]:
                if str(cart_item.product.id) == item["product_id"]:
                    cart_item.quantity = item["quantity"]
                    cart_item.save()
                    break
            else:
                new_prod = {
                    "product_id": str(cart_item.product.id),
                    "quantity": cart_item.quantity,
                }
                self.cart["items"].append(new_prod)
        self.cart_merge(user=user)
        self.save()

    def cart_merge(self, user):
        cart_model, created = CartModel.objects.get_or_create(user=user)
        for item in self.cart["items"]:
            product_obj = ProductModel.objects.get(
                id=item["product_id"], status=ProductStatus.active.value
            )
            cart_item, created = CartItemModel.objects.get_or_create(
                cart=cart_model, product=product_obj
            )
            cart_item.quantity = item["quantity"]
            cart_item.save()
        session_product_ids = [
            item["product_id"] for item in self.cart["items"]
        ]
        CartItemModel.objects.filter(cart=cart_model).exclude(
            product__id__in=session_product_ids
        ).delete()
