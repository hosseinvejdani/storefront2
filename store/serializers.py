from rest_framework import fields, serializers
from .models import Cart, CartItem, Product, Collection, Review
from decimal import Decimal

class ReviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','created_at','name','description']

    def create(self,validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)


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


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price']

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = CartItem
        fields = ['id','product','quantity','total_price']

    def get_total_price(self,cart_item: CartItem):
        return cart_item.product.unit_price * cart_item.quantity

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields = ['id','items','total_price']

    def get_total_price(self, cart : Cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])