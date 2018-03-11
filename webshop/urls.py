"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from api.resources import CustomerResource, ProductResource, OrderResource, OrderDetailResource
import api.views as views

v1_api = Api(api_name='v1')
v1_api.register(CustomerResource())
v1_api.register(ProductResource())
v1_api.register(OrderResource())
v1_api.register(OrderDetailResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include(customer_resource.urls)),
    url(r'^api/', include(v1_api.urls)),
    # url(r'^api/v1/product/add', views.add_product),
    url(r'^api/v1/customer/(?P<customer_id>\w[\w/-]*)/order/add', views.add_product),
    url(r'^api/v1/customer/(?P<customer_id>\w[\w/-]*)/order/update', views.update_product),
    url(r'^api/v1/customer/(?P<customer_id>\w[\w/-]*)/order_history', views.order_history),
    url(r'^api/v1/customer/(?P<customer_id>\w[\w/-]*)/order/(?P<order_id>\w[\w/-]*)/details', views.order_details),
    url(r'^api/v1/customer/(?P<customer_id>\w[\w/-]*)/order/(?P<order_id>\w[\w/-]*)/checkout', views.checkout),
    url(r'^api/v1/customer/(?P<customer_id>\w[\w/-]*)/order/cart', views.current_cart)
]
