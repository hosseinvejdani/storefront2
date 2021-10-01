from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        # use select_related for nested format too.
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')

@api_view()
def product_details(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product,context={'request': request})
    return Response(serializer.data)


@api_view()
def collection_details(request,pk):
    return  Response('ok')