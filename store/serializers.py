from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['id','title','unit_price','collection']   # -> original fields from model 
        fields = ['id','title','unit_price','price_with_tax','collection']  # -> overrided fields

    # we can override one of more field like this:
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_price_with_tax')
    collection = CollectionSerializer()
    
    def calculate_price_with_tax(self,product: Product):
        return product.unit_price * Decimal(1.1)
