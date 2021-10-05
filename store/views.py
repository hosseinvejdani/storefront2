from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Product, Collection, Review
from .filters import ProductFilter
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerialize


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerialize

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title','description']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request,*args,**kwargs):
        product = get_object_or_404(Product, pk = kwargs['pk'])
        if product.orderitem_set.count()>0:
            msg = 'method can not be applied becouse there are one or more order item associated with this product'
            return Response({'error':msg},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request,*args,**kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionSerializer

    def destroy(self, request,*args,**kwargs):
        collection = get_object_or_404(Collection, pk = kwargs['pk'])
        if collection.product_set.count()>0:
            msg = 'this collection can not be delete becouse it containes one or more products in it'
            return Response({'error':msg},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request,*args,**kwargs)
    





