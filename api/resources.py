from tastypie.resources import ModelResource
from api.models import Customer, Product, Order, OrderDetail
from tastypie.authorization import Authorization
from tastypie import fields

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
  # order_id = fields.ToManyField(OrderDetailResource, attribute='order_id', full=True, null=True)
  class Meta:
    queryset = Order.objects.all()
    resource_name = 'order'
    authorization = Authorization()

class OrderDetailResource(ModelResource):
  # order_id = fields.ForeignKey(OrderResource, attribute='order_id', full=True, null=True)
  # product_id = fields.ForeignKey(ProductResource, attribute='product_id', full=True, null=True)
  class Meta:
    queryset = OrderDetail.objects.all()
    resource_name = 'orderdetail'
    authorization = Authorization()


