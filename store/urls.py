from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>', views.ProductDetails.as_view()),
    path('collections/', views.collection_list),
    path('collections/<int:pk>', views.collection_details)
]
