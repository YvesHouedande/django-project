# core/urls.py

from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings


urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('connexion/', views.user_login, name='login'),
    path('cat/<str:category_name>/', views.filter_products, name='filter_product_cat'),
    re_path(r'^filter/(?:(?P<kind>[\w-]+)/)?$', views.filter_products, name='filter_products'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path("restaure/", views.add_to_cart),
    path("listPanier/", views.listPanier, name="listPanier"),
    path("HandleOrder/", views.handle_order, name="HandleOrder"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
