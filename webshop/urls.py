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
from api.resources import CustomerResource, ProductResource, OrderResource, OrderDetailResource

customer_resource = CustomerResource()
product_resource = ProductResource()
order_resource = OrderResource()
order_detail_resource = OrderDetailResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(customer_resource.urls)),
    url(r'^api/', include(product_resource.urls)),
    url(r'^api/', include(order_resource.urls)),
    url(r'^api/', include(order_detail_resource.urls))
]
