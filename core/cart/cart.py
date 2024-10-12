from shop.models import ProductModel,ProductStatus

class CartSession:
    def __init__(self, session):
        self.session = session
        self.cart = self.session.setdefault('cart',
        {
            'items':[],
            'total_price':0,
            'total_items':0,
        })

    def add_prod(self, product_id):
        for item in self.cart['items']:
            if product_id == item['product_id']:
                item['quantity'] += 1
                break
        else:
            new_prod = {
                'product_id': product_id,
                'quantity': 1,
            }
            self.cart['items'].append(new_prod)
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

    def clear(self):
        self.cart = self.session['cart'] = {
            'items':[],
            'total_price':0,
            'total_items':0,
        }
        self.save()

    def save(self):
        self.session.modified = True
