from django.views.generic import TemplateView,UpdateView,ListView,DeleteView,CreateView,DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from ..permissions import AdminPermissions
from .form import ChangePassForm,ProfileForm,AdminEditProductForm,AdminCouponForm,AdminMemberEditForm
from accounts.models import User,Profile,UserType
from shop.models import ProductModel,CategoryModel
from order.models import OrderModel,CouponModel
from django.core.exceptions import FieldError

class AdminDashboard(LoginRequiredMixin,AdminPermissions,TemplateView):
    template_name = 'dashboard/admin/home.html'

class ChangePassView(LoginRequiredMixin,AdminPermissions,SuccessMessageMixin,PasswordChangeView):
    template_name = 'dashboard/admin/profile/change-pass.html'
    form_class = ChangePassForm
    success_url = reverse_lazy("dashboard:admin:change-pass")
    success_message = 'Password changed successfully'

class ProfileView(LoginRequiredMixin,AdminPermissions,UpdateView,SuccessMessageMixin):
    template_name = 'dashboard/admin/profile/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = 'Profile changed successfully'

    def get_object(self, queryset = None):
        return Profile.objects.get(user = self.request.user)

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
    

class OrdersList(LoginRequiredMixin,AdminPermissions,ListView):
    queryset = OrderModel.objects.all()
    template_name = 'dashboard/admin/orders/list.html'
    context_object_name = 'orders'

    paginate_by = 5
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    
class OrderSingle(LoginRequiredMixin,AdminPermissions,DetailView):
    model = OrderModel
    template_name = 'dashboard/admin/orders/single.html'
    context_object_name = 'order'


class AdminCouponView(LoginRequiredMixin,AdminPermissions,ListView):
    template_name = 'dashboard/admin/coupons/coupon-list.html'
    context_object_name = 'coupons' 

    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = CouponModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(code__icontains=search_q)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    

class AdminCouponCreateView(LoginRequiredMixin,AdminPermissions,CreateView,SuccessMessageMixin):
    queryset = CouponModel.objects.all()
    template_name = 'dashboard/admin/coupons/coupon-create.html'
    form_class = AdminCouponForm
    success_url = reverse_lazy("dashboard:admin:coupon-list")
    success_message = 'کد تخفیف با موفقیت ایجاد شد'


class AdminMemberListView(LoginRequiredMixin,AdminPermissions,ListView):
    template_name = 'dashboard/admin/members/member-list.html'
    context_object_name = 'members'

    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = User.objects.all().exclude(email=self.request.user.email).exclude(user_type = UserType.superuser.value)
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(email__icontains=search_q)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    

class AdminMemberEditView(LoginRequiredMixin,AdminPermissions,UpdateView,SuccessMessageMixin):
    template_name = 'dashboard/admin/members/member-edit.html'
    form_class = AdminMemberEditForm
    success_message = 'کاربر با موفقیت ویرایش شد'

    def get_queryset(self):
        return User.objects.all().exclude(email=self.request.user.email).exclude(user_type = UserType.superuser.value)

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:member-edit",kwargs={'pk':self.get_object().pk})