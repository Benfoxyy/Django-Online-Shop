from itertools import product
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from shop.sitemaps import ProductSitemap

sitemaps = {"static": StaticViewSitemap, "products": ProductSitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("website.urls")),
    path("accounts/", include("accounts.urls")),
    path("shop/", include("shop.urls")),
    path("cart/", include("cart.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("order/", include("order.urls")),
    path("payment/", include("payment.urls")),
    path("review/", include("review.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

handler404 = "core.error_views.error_404"

if settings.DEBUG:
    import debug_toolbar
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Django Online Shop API",
            default_version="v1",
            description="you can use it by any front end framework like (React, Vue, Angular, ...)",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="benxfoxy@gmail.com"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        path(
            "swagger<format>/",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
