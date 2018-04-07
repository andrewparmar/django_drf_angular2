# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product , Location ,Family ,Transaction 
from .serializers import *

from rest_framework import status , generics , mixins

# Create your views here.
class product_list(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class product_detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class family_list(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

# class family_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class family_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class location_list(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class location_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class =  LocationSerializer

class transaction_list(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class transaction_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class =  TransactionSerializer