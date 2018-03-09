from tastypie.resources import ModelResource
from api.models import Customer, Product, Order, OrderDetail
from tastypie.authorization import Authorization

class CustomerResource(ModelResource):
  class Meta:
    queryset = Customer.objects.all()
    resource_name = 'customer'
    authorization = Authorization()

class ProductResource(ModelResource):
  class Meta:
    queryset = Product.objects.all()
    resource_name = 'product'
    authorization = Authorization()
  
class OrderResource(ModelResource):
  class Meta:
    queryset = Order.objects.all()
    resource_name = 'order'
    authorization = Authorization()

class OrderDetailResource(ModelResource):
  class Meta:
    queryset = OrderDetail.objects.all()
    resource_name = 'orderdetail'
    authorization = Authorization()