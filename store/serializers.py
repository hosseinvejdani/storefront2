from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','products_count']

    products_count = serializers.IntegerField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['id','title','unit_price','collection']   # -> original fields from model 
        fields = ['id','title','slug','unit_price','price_with_tax','inventory','collection']  # -> overrided fields

    # we can override one of more field like this:
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_price_with_tax')
    collection = serializers.PrimaryKeyRelatedField(
        queryset = Collection.objects.all()
    )
    
    def calculate_price_with_tax(self,product: Product):
        return product.unit_price * Decimal(1.1)
