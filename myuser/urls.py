from django.urls import path

from . import views

urlpatterns = [
    path('cart/<userid>/<category>/<productid>',views.cart,name="cart"),
    path('mycart',views.mycart,name="mycart"),
    path('delcart/<tablename>/<productid>',views.delcart,name="delcart"),
    path('buynow/<category>/<productid>',views.buynow,name="buynow"),
    path('buynow/<category>/placeorder/<category1>/<productid>',views.placeorder,name="placeorder"),
    path('opsuccess/<category>/<productid>',views.opsuccess,name="opsuccess"),
    path('cartconfirmation/<price>',views.cartconfirmation,name="cartconfirmation"),
    path('cartconfirmation/cart/payment',views.cartpayment,name="cartpayment"),
    path('clearcart',views.clearcart,name="clearcart"),
    path('cartonlinepay',views.cartonlinepay,name="cartonlinepay"),
    path('success',views.success,name="success"),
    path('myorders',views.myorders,name="myorders"),
   
]
