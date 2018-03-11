# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Customer(models.Model):
  id = models.AutoField(primary_key = True)
  first_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  phone_number = models.CharField(max_length=50, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s %s' % (self.first_name, self.last_name)

class Product(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length=200, null=True)
  unit_cost = models.FloatField(default=0)
  properties = JSONField(default={}, null=True)
  inventory = models.PositiveIntegerField(default=0)
  sku = models.CharField(max_length=20, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s %i %i' % (self.name, self.inventory, self.unit_cost)

class Order(models.Model):
  id = models.AutoField(primary_key = True)
  customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
  total_cost = models.FloatField(default=0)
  shipping_address = models.CharField(max_length=200, null=True)
  comments = models.TextField(blank=True, null=True)
  status = models.PositiveIntegerField(default=0)
  completed = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return  '%i %i' % (self.total_cost, self.status)

class OrderDetail(models.Model):
  id = models.AutoField(primary_key = True)
  order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%i %i %s %i' % (self.order_id.id, self.product_id.id, self.product_id.name, self.quantity)