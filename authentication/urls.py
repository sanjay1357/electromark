from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('otpgenerate/', views.otpgenerate, name="otpgenerate"),
    path('accountcreate', views.accountcreate, name="login"),
    path('forgot', views.forgot, name="forgot"),
    path('forgototp/', views.forgototp, name="forgototp"),
    path('pwdchange', views.pwdchange, name="pwdchange"),
    path('editprofile', views.editprofile, name="editprofile"),
    path('logout', views.logout, name="logout"),
    path('updatelocation', views.updatelocation, name="updatelocation"),
    path('checktracking/',views.checktracking,name="checktracking"),
]
