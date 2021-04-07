from django.urls import path

from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('viewproduct', views.viewproduct, name="viewproduct"),
    path('addproduct', views.addproduct, name="addproduct"),
    path('adding', views.adding, name="adding"),
    path('productvalidate/', views.productvalidate, name="productvalidate"),
    path('allproduct/<category>', views.allproduct, name="allproduct"),
    path('allproduct/filter/<category>', views.filter, name="filter"),
    path('allproduct/description/<category>/<id>', views.description, name="description"),
    path('search',views.search,name="search"),
]
