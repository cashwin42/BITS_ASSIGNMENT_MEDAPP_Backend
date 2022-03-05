from django.shortcuts import render
from healthappdata.models import Meds
from healthappdata.models import Order
from healthappdata.models import Transaction
from healthappdata.models import CartNumber
from healthappdata.serializers import MedsSerializer
from healthappdata.serializers import OrderSerializer
from healthappdata.serializers import TransactionSerializer
from healthappdata.serializers import CartNumberSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

class MedstList(generics.ListCreateAPIView):
    queryset = Meds.objects.all()
    serializer_class = MedsSerializer
class MedsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meds.objects.all()
    serializer_class = MedsSerializer

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CartNumberList(generics.ListCreateAPIView):
    queryset = CartNumber.objects.all()
    serializer_class = CartNumberSerializer
class CartNumberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartNumber.objects.all()
    serializer_class = CartNumberSerializer


