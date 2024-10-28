from django.views.generic import TemplateView,UpdateView,ListView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from ..permissions import AdminPermissions
from .form import ChangePassForm,ProfileForm
from accounts.models import Profile
from shop.models import ProductModel,ProductStatus,CategoryModel
from django.core.exceptions import FieldError

class AdminDashboard(AdminPermissions,TemplateView):
    template_name = 'dashboard/admin/home.html'

class ChangePassView(AdminPermissions,SuccessMessageMixin,PasswordChangeView):
    template_name = 'dashboard/admin/profile/change-pass.html'
    form_class = ChangePassForm
    success_url = reverse_lazy("dashboard:admin:change-pass")
    success_message = 'Password changed successfully'

class ProfileView(AdminPermissions,UpdateView,SuccessMessageMixin):
    template_name = 'dashboard/admin/profile/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = 'Profile changed successfully'

    def get_object(self, queryset = None):
        return Profile.objects.get(user = self.request.user)
    
class ProfileEditView(AdminPermissions,UpdateView,SuccessMessageMixin):
    http_method_names = ['post']
    model = Profile
    fields = ['avatar']
    success_url = reverse_lazy("dashboard:admin:home")
    success_message = 'Profile picture changed successfully'

    def get_object(self, queryset = None):
        return Profile.objects.get(user = self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,'وایییی')
        return redirect(self.success_url)
    

class AdminShowProducts(AdminPermissions,ListView):
    template_name = 'dashboard/admin/products/show-products.html'
    paginate_by = 2
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = ProductModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)
        if minprice_q := self.request.GET.get("min_price"):
            queryset = queryset.filter(price__gte=minprice_q)
        if maxprice_q := self.request.GET.get("max_price"):
            queryset = queryset.filter(price__lte=maxprice_q)
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
