from rest_framework import serializers
from healthappdata.models import Meds
from healthappdata.models import Order
from healthappdata.models import Transaction
from healthappdata.models import CartNumber


class MedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meds
        fields=["id","name","stock","price","prescription"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=["id","medName","quantity","dateOrdered","delivered","price"]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields=["id","key","status","dateOrdered","expectedDeliveryDate","currentStatus"]

class CartNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartNumber
        fields=["cartItemsNumber","id"]
