from shop.models import ProductModel,ProductStatus
from decimal import Decimal

class CartSession:
    def __init__(self, session):
        self.session = session
        self.cart = self.session.setdefault('cart',
        {
            'items':[],
            'total_price':0,
            'total_items':0,
        })

    def add_prod(self, product_id, quantity = None):
        for item in self.cart['items']:
            if product_id == item['product_id']:
                if quantity is None:
                    item['quantity'] += 1
                else:
                    item['quantity'] += int(quantity)
                break
        else:
            new_prod = {
                'product_id': product_id,
                'quantity': 1,
            }
            self.cart['items'].append(new_prod)
        self.save()

    def del_prod(self, product_id):
        for item in self.cart['items']:
            if product_id == item['product_id']:
                self.cart['items'].remove(item)
                break
        else:
            return
        self.save()

    def get_cart(self):
        return self.cart
    
    def get_cart_items(self):
        for item in self.cart['items']:
            prod_obj = ProductModel.objects.get(id=item['product_id'],status=ProductStatus.active.value)
            item.update({'prod_obj': prod_obj})
        
        return self.cart['items']
    
    def get_cart_quantity(self):
        return sum(item['quantity'] for item in self.cart['items'])
    
    def get_total_price(self):
        items = self.get_cart_items()
        for item in items:
            if not item.get('prod_obj').discount_percent:
                self.cart['total_price'] += item.get('prod_obj').price * item.get('quantity')
            else:
                self.cart['total_price'] += item.get('prod_obj').offer() * item.get('quantity')
        tax = self.cart['total_price'] * Decimal('0.09')
        
        return int(self.cart['total_price'] + tax)
    
    def change_prod_quantity(self, product_id, quantity):
        for item in self.cart['items']:
            if product_id == item['product_id']:
                item['quantity'] = int(quantity)
                break
        else:
            return
        self.save()

    def clear(self):
        self.cart.update({
            'items': [],
            'total_price': 0,
            'total_items': 0,
        })
        
        self.save()

    def save(self):
        self.session.modified = True
