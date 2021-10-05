from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer

class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    # def destroy(self,request,pk):
    #     product = get_object_or_404(Product,pk=pk)
    #     if product.orderitem_set.count()>0:
    #         return Response({'error':'method can not be applied becouse there are one or more order item associated with this product'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # ====  OR Try This =====================

    def destroy(self, request,*args,**kwargs):
        # product = get_object_or_404(Product,pk=pk)  # this is magical part of django
        if product.orderitem_set.count()>0:
            return Response({'error':'method can not be applied becouse there are one or more order item associated with this product'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request,*args,**kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionSerializer

    # def destroy(self, request, pk):
    #     collection = get_object_or_404(Collection,pk=pk)
    #     if collection.product_set.count()>0:
    #         msg = 'this collection can not be del;etd becouse it containes one or more products in it'
    #         return Response({'error':msg},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


    # ====  OR Try This =====================

    def destroy(self, request,*args,**kwargs):
        # collection = get_object_or_404(Collection,pk=kwargs['pk']) # this is magical part of django
        if collection.product_set.count()>0:
            msg = 'this collection can not be del;etd becouse it containes one or more products in it'
            return Response({'error':msg},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request,*args,**kwargs)
    





