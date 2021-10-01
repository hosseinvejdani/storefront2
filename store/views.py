from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view()
def product_list(request):
    return Response('ok')


@api_view()
def product_details(request,id):
    try:
        product = Product.objects.get(pk = id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        # return Response(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)