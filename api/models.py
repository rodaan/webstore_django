# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Customer(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  phone_number = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s %s' % (self.first_name, self.last_name)

class Product(models.Model):
  name = models.CharField(max_length=200)
  unit_cost = models.FloatField()
  properties = JSONField()
  inventory = models.PositiveIntegerField()
  sku = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s %i %i' % (self.name, self.inventory, self.unit_cost)

class Order(models.Model):
  customer_id = models.ForeignKey(Customer)
  total_cost = models.FloatField()
  shipping_address = models.CharField(max_length=200)
  comments = models.TextField()
  status = models.PositiveIntegerField()
  completed = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%i %i %i' % (self.customer_id, self.total_cost, self.status)

class OrderDetail(models.Model):
  order_id = models.ForeignKey(Order)
  product_id = models.ForeignKey(Product)
  quantity = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%i %i %i' % (self.order_id, self.product_id, self.quantity)