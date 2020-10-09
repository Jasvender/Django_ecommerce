"""ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from carts.views import cart_home, cart_detail_api_view
from billing.views import payment_method_view
from accounts.views import LoginView, RegisterView, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from .views import home_page, contact_page, project_page

urlpatterns = [
    path('', home_page, name="home"),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include("accounts.urls", namespace='accounts')),
    path('contact/', contact_page, name="contact"),
    path('project/', project_page, name="project"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/guest/', guest_register_view, name="guest_register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('blogs/', include("blogs.urls", namespace="blogs")),
    path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls", namespace='search')),
    path('cart/', include("carts.urls", namespace='cart')),
    path('api/cart/', cart_detail_api_view, name="api-cart"),
    path('billing/payment-method/', payment_method_view, name="payment-method-view"),
    path('checkout/address/create', checkout_address_create_view, name="checkout_address_create"),
    path('checkout/address/reuse', checkout_address_reuse_view, name="checkout_address_reuse_view"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
     urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)