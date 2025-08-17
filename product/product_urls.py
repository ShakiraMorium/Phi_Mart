from django.urls import path
from product import views


urlpatterns = [
    
        path('', views.ProductViewSet.as_view() , name='product-list'),
        # path('<int:id>/', views.ProductDetails.as_view(), name='products-list'),
    
]  

