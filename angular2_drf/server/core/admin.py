# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Product, Family, Transaction, Location

admin.site.register(Product)
admin.site.register(Family)
admin.site.register(Transaction)
admin.site.register(Location)