# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from api.models import Order
# Create your views here.
@require_http_methods(["GET", "POST"])
def update_cart(request):
  # get current cart from cache if current cart does not exist, make a new one
  if Order.objects.filter(id=request.body.customer_id, status=0)
    cart = Order.objects.filter(id=request.body.customer_id, status=0)
  else
    cart = Order()

  
  # check request object for item 
  print(request.body)
  test = 'hi'
  if request.body == "add":
    test = 'cool'
    
  return JsonResponse({'something': test})