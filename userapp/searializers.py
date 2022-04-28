from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User,Seller

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
class Sellerserializers(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields='__all__'