# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from api.models import Order, Product, Customer, OrderDetail
import datetime
from django.utils.timezone import utc

# add product to cart and creates cart if cart doesn't exist
@require_http_methods(["GET", "POST"])
def add_product(request, customer_id):
  # get current cart from cache if current cart does not exist, make a new one
  jsonObj = json.loads(request.body)
  product_id = jsonObj['product_id']
  quantity = jsonObj['quantity']
  product = Product.objects.filter(id=product_id)[0]
  if quantity > product.inventory:
    data = { "error": "not enough inventory"}
  else:
    if Order.objects.filter(customer_id=customer_id, status=0):
      cart = Order.objects.filter(customer_id=customer_id, status=0)[0]
    else:
      current_customer = Customer.objects.filter(id=customer_id)[0]
      cart = Order(status=0, customer_id=current_customer)
    # check request object for item
    cart.total_cost = cart.total_cost + (product.unit_cost * quantity)
    cart.save()
    od = OrderDetail(order_id=cart, product_id=product, quantity=quantity)
    od.save()
    data = serializers.serialize("json", [od,])
  return JsonResponse(data, safe=False)

# update cart contents
@require_http_methods(["POST"])
def update_product(request, customer_id):
  jsonObj = json.loads(request.body)
  product_id = jsonObj['product_id']
  quantity = jsonObj['quantity']
  product = Product.objects.filter(id=product_id)[0]
  if Order.objects.filter(customer_id=customer_id, status=0):
    cart = Order.objects.filter(customer_id=customer_id, status=0)[0]
    # check to see if quantity is larger or smaller
    orderdetail = OrderDetail.objects.filter(order_id=cart.id, product_id=product_id)[0]
    if quantity == 0:
      cart.total_cost = cart.total_cost - (orderdetail.quantity * product.unit_cost)
      cart.save()
      orderdetail.delete()
      data = {"status": "completed"}
    elif quantity > product.inventory:
      data = {"error": "not enough inventory"}
    else:
      difference = quantity - orderdetail.quantity
      orderdetail.quantity = quantity
      orderdetail.save()
      cart.total_cost = cart.total_cost + (difference * product.unit_cost)
      cart.save()
      data = serializers.serialize("json", [orderdetail,])
  else:
    data = {"error": "not found"}
  return JsonResponse(data, safe=False)

# return list of historical orders by customer_id
@require_http_methods(["GET"])
def order_history(request, customer_id):
  orders = Order.objects.filter(customer_id=customer_id, status=3)
  data = serializers.serialize("json", orders)
  return JsonResponse(data, safe=False) 

# return details of a specific order
@require_http_methods(["GET"])
def order_details(request, customer_id, order_id):
  order = Order.objects.filter(customer_id=customer_id, id=order_id)
  order_details = OrderDetail.objects.filter(order_id=order_id)
  data = serializers.serialize("json", order_details)
  order_data = serializers.serialize("json", order)
  resObj = {"order": data, "order_details": order_data}
  return JsonResponse(resObj, safe=False)

# complete purchase of items
@require_http_methods(["POST"])
def checkout(request, customer_id, order_id):
  jsonObj = json.loads(request.body)
  shipping_address = jsonObj['shipping_address']
  if Order.objects.filter(customer_id=customer_id, status=0):
    cart = Order.objects.filter(customer_id=customer_id, status=0)[0]
    # reduce inventory amount
    order_details = OrderDetail.objects.filter(order_id=cart.id)
    for order_detail in order_details:
      product = Product.objects.filter(id=order_detail.product_id.id)[0]
      product.inventory = product.inventory - order_detail.quantity
      product.save()
    cart.shipping_address = shipping_address
    cart.status = 3
    cart.completed = datetime.datetime.utcnow().replace(tzinfo=utc)
    cart.save()
    data = serializers.serialize("json", [cart,])
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse({"error": "cart is empty"})
  