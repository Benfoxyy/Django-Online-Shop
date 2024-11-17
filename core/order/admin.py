from django.contrib import admin
from .models import *

admin.site.register(OrderModel)
admin.site.register(OrderItemsModel)
admin.site.register(AddressModel)
admin.site.register(CouponModel)