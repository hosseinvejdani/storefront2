from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('customers', views.CustomerViewSet)
router.register('carts', views.CartViewSet,basename='carts')
router.register('orders', views.OrderViewSet)

product_router=routers.NestedDefaultRouter(router, 'products',lookup='product')
product_router.register('reviews', views.ReviewViewSet,basename='product-review')

cart_router=routers.NestedDefaultRouter(router, 'carts',lookup='cart')
cart_router.register('items', views.CartItemViewSet,basename='cart-items')

urlpatterns = router.urls + product_router.urls + cart_router.urls

# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>', views.ProductDetails.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>', views.CollectionDetails.as_view())
# ]
