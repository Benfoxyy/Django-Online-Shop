from django.views import generic
from django.db.models import Count, Q
from review.models import ReviewModel
from .models import ProductModel, ProductStatus, CategoryModel, WishListModel
from django.core.exceptions import FieldError
from cart.cart import CartSession
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# @method_decorator(cache_page(60 * 15), name="dispatch")
class ShopProductGridListView(generic.ListView):
    template_name = "shop/products-grid.html"
    paginate_by = 9

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)

    def get_queryset(self):
        queryset = ProductModel.objects.filter(
            status=ProductStatus.active.value,
        )
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
        context = super().get_context_data(**kwargs)
        context["total_prod"] = self.get_queryset().count()
        context["is_wished"] = (
            WishListModel.objects.filter(user=self.request.user).values_list(
                "product_id", flat=True
            )
            if self.request.user.is_authenticated
            else []
        )
        context["categories"] = CategoryModel.objects.all()
        return context


# @method_decorator(cache_page(60 * 15), name="dispatch")
class ShopProductListView(generic.ListView):
    template_name = "shop/products-list.html"
    paginate_by = 9

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)

    def get_queryset(self):
        queryset = ProductModel.objects.filter(
            status=ProductStatus.active.value
        )
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
        context = super().get_context_data(**kwargs)
        context["total_prod"] = self.get_queryset().count()
        context["is_wished"] = (
            WishListModel.objects.filter(user=self.request.user).values_list(
                "product_id", flat=True
            )
            if self.request.user.is_authenticated
            else []
        )
        context["categories"] = CategoryModel.objects.all()
        return context


# @method_decorator(cache_page(60 * 15), name="dispatch")
class ShopProductDetailView(generic.DeleteView):
    template_name = "shop/product_detail.html"
    queryset = ProductModel.objects.filter(status=ProductStatus.active.value)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = ReviewModel.objects.filter(product=self.get_object())
        one_star = Count("rate", filter=Q(rate=1))
        two_star = Count("rate", filter=Q(rate=2))
        three_star = Count("rate", filter=Q(rate=3))
        four_star = Count("rate", filter=Q(rate=4))
        five_star = Count("rate", filter=Q(rate=5))
        context["reviews"] = reviews
        context["reviews_status"] = reviews.aggregate(
            one_star=one_star,
            two_star=two_star,
            three_star=three_star,
            four_star=four_star,
            five_star=five_star,
        )
        return context


class AddOrRemoveWish(generic.View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        if product_id:
            wish_obj, created = WishListModel.objects.get_or_create(
                user=request.user, product_id=product_id
            )
            message = "محصول به لیست علایق اضافه شد"
            if not created:
                wish_obj.delete()
                message = "محصول از لیست علایق حذف شد"
        return JsonResponse({"message": message})
