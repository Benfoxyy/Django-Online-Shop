from django.views.generic import UpdateView,ListView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from ...permissions import AdminPermissions
from shop.models import ProductModel,CategoryModel
from ..forms import *


class AdminShowProducts(LoginRequiredMixin,AdminPermissions,ListView):
    template_name = 'dashboard/admin/products/show-products.html'
    paginate_by = 2
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = ProductModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)
        if category_id := self.request.GET.get("category_id"):
            queryset = queryset.filter(category__id=category_id)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['total_prod']= self.get_queryset().count()
        context['categories']= CategoryModel.objects.all()
        return context


class AdminEditProducts(LoginRequiredMixin,AdminPermissions,UpdateView,SuccessMessageMixin):
    queryset = ProductModel.objects.all()
    template_name = 'dashboard/admin/products/edit-products.html'
    form_class = AdminEditProductForm
    
    def get_success_url(self):
        return reverse_lazy("dashboard:admin:edit-prod",kwargs={'pk':self.get_object().pk})
    

class AdminDeleteProducts(LoginRequiredMixin,AdminPermissions,DeleteView,SuccessMessageMixin):
    queryset = ProductModel.objects.all()
    template_name = 'dashboard/admin/products/delete-prod.html'
    success_url = reverse_lazy('dashboard:admin:show-prod')
    success_message = 'Product successfuly deleted'


class AdminCreateProducts(LoginRequiredMixin,AdminPermissions,CreateView,SuccessMessageMixin):
    queryset = ProductModel.objects.all()
    template_name = 'dashboard/admin/products/create-product.html'
    form_class = AdminEditProductForm
    success_url = reverse_lazy("dashboard:admin:show-prod")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)