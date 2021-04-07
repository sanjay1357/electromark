from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Cart,Order
from django.contrib.auth.models import User, auth
from products.models import Mobiles,Tv,Pc,Accessories,Appliances
from django.db.models import Sum
from authentication.models import Users
import random
import datetime
import time
# Create your views here.

def success(request):
    
    return render(request,'success.html')


def clearcart(request):
    
    userid=request.user.id
    Cart.objects.filter(userid=userid).delete()
    return redirect("mycart")



def cart(request,userid,category,productid):
    if category=="TV":
        if Cart.objects.filter(userid=userid,tablename="Tv",productid=productid).exists():
                return render(request,'alreadycart.html')
        else:
           c=Cart(userid=userid,tablename="Tv",productid=productid)
           c.save()


    elif category=="MOBILES" or category=="TABLETS":
        if Cart.objects.filter(userid=userid,tablename="Mobiles",productid=productid).exists():
                return render(request,'alreadycart.html')
        else:
           c=Cart(userid=userid,tablename="Mobiles",productid=productid)
           c.save()


    elif category=="PC":
        if Cart.objects.filter(userid=userid,tablename="Pc",productid=productid).exists():
                return render(request,'alreadycart.html')
        else:
           c=Cart(userid=userid,tablename="Pc",productid=productid)
           c.save()


    elif category=="APPLIANCES":
        if Cart.objects.filter(userid=userid,tablename="Appliances",productid=productid).exists():
                return render(request,'alreadycart.html')
        else:
           c=Cart(userid=userid,tablename="Appliances",productid=productid)
           c.save()
    else:
        if Cart.objects.filter(userid=userid,tablename="Accessories",productid=productid).exists():
                return render(request,'alreadycart.html')
        else:
           c=Cart(userid=userid,tablename="Accessories",productid=productid)
           c.save()
    
    return redirect("mycart")


def mycart(request):
    userid=request.user.id
    one=Cart.objects.filter(userid=userid,tablename="Tv")
    two=Cart.objects.filter(userid=userid,tablename="Mobiles")
    three=Cart.objects.filter(userid=userid,tablename="Pc")
    four=Cart.objects.filter(userid=userid,tablename="Accessories")
    five=Cart.objects.filter(userid=userid,tablename="Appliances")

    
       
    tv=Tv.objects.filter(id__in=[f.productid for f in one],stock__gte=1)
    mobiles=Mobiles.objects.filter(id__in=[f.productid for f in two],stock__gte=1)
    pc=Pc.objects.filter(id__in=[f.productid for f in three],stock__gte=1)
    accessories=Accessories.objects.filter(id__in=[f.productid for f in four],stock__gte=1)
    appliances=Appliances.objects.filter(id__in=[f.productid for f in five],stock__gte=1)
    price=0
    if tv: 
      for i in tv:
          price+=i.curprice
    if mobiles: 
      for i in mobiles:
          price+=i.curprice
    if pc: 
     for i in pc:
          price+=i.curprice
    if accessories: 
      for i in accessories:
          price+=i.curprice
    if appliances: 
      for i in appliances:
          price+=i.curprice
    a="Mobiles"
    b="Accessories"
    c="Appliances"
    d="Tv"
    e="Pc"
    testing="TV"

    return render(request,'cart.html',{'mobiles':mobiles,'tv':tv,'pc':pc,'accessories':accessories,'appliances':appliances,'a':a,'b':b,'c':c,'d':d,'e':e,'price':price,'testing':testing})


def delcart(request,tablename,productid):
    userid=request.user.id
    Cart.objects.filter(userid=userid,tablename=tablename,productid=productid).delete()
    return redirect("mycart")

def buynow(request,category,productid):
    
    mid=int(request.user.first_name)
    add=Users.objects.get(id=mid)
    if category=="MOBILES":
        obj=Mobiles.objects.get(id=productid)
    elif category=="PC":
        obj=Pc.objects.get(id=productid)
    elif category=="TV":
        obj=Tv.objects.get(id=productid)
    elif category=="ACCESSORIES":
        obj=Accessories.objects.get(id=productid)
    elif category=="APPLIANCES":
        obj=Appliances.objects.get(id=productid)
    else:
        return HttpResponse("error in buynow order")
    return render(request,'confirmation.html',{'category1':category,'obj':obj,'add':add})


def placeorder(request,category,category1,productid):
    if request.method=='POST':
        x=str(time.ctime())
        j=0
        while j<=10:
              tracking=random.randint(1,99999999)
              if Order.objects.filter(tracking=tracking).exists():
                  print("exists")
              else:
                  break

        mode=request.POST['mode']
        userid=request.user.id
        if mode=="cod":
            if category1=="MOBILES":
               obj=Mobiles.objects.get(id=productid)
              
            elif category1=="PC":
               obj=Pc.objects.get(id=productid)
               
            elif category1=="TV":
               obj=Tv.objects.get(id=productid)
            elif category1=="ACCESSORIES":
               obj=Accessories.objects.get(id=productid)
            elif category1=="APPLIANCES":
               obj=Appliances.objects.get(id=productid)
            else:
                return HttpResponse("error in place order")
            names=obj.name
            obj.stock=obj.stock-1
            obj.save()
            o=Order(userid=userid,tablename=category1,name=names,productid=productid,status="ordered",times=x,tracking=tracking,payment="cod")
            o.save()
            return render(request,'success.html')

        else:
            return render(request,'onlinepayment.html',{'category':category1,'productid':productid})
            

def opsuccess(request,category,productid):
    if category=="MOBILES":
        obj=Mobiles.objects.get(id=productid)
    elif category=="PC":
        obj=Pc.objects.get(id=productid)
    elif category=="TV":
        obj=Tv.objects.get(id=productid)
    elif category=="ACCESSORIES":
        obj=Accessories.objects.get(id=productid)
    elif category=="APPLIANCES":
        obj=Appliances.objects.get(id=productid)
    else:
        return HttpResponse("online payment page error occurs")
    names=obj.name
    x=str(time.ctime())
    j=0
    while j<=10:
          tracking=random.randint(1,99999999)
          if Order.objects.filter(tracking=tracking).exists():
             print("exists")
          else:
             break

    userid=request.user.id
    obj.stock=obj.stock-1
    obj.save()
    o=Order(userid=userid,tablename=category,name=names,productid=productid,status="ordered",times=x,tracking=tracking,payment="op")
    o.save()
    return render(request,'success.html')


def cartconfirmation(request,price):
    another=int(request.user.first_name)
    add=Users.objects.get(id=another)
    userid=request.user.id
    one=Cart.objects.filter(userid=userid,tablename="Tv")
    two=Cart.objects.filter(userid=userid,tablename="Mobiles")
    three=Cart.objects.filter(userid=userid,tablename="Pc")
    four=Cart.objects.filter(userid=userid,tablename="Accessories")
    five=Cart.objects.filter(userid=userid,tablename="Appliances")

    
       
    tv=Tv.objects.filter(id__in=[f.productid for f in one],stock__gte=1)
    mobiles=Mobiles.objects.filter(id__in=[f.productid for f in two],stock__gte=1)
    pc=Pc.objects.filter(id__in=[f.productid for f in three],stock__gte=1)
    accessories=Accessories.objects.filter(id__in=[f.productid for f in four],stock__gte=1)
    appliances=Appliances.objects.filter(id__in=[f.productid for f in five],stock__gte=1)



    return render(request,'cartconfirmation.html',{'price':price,'add':add,'mobiles':mobiles,'tv':tv,'pc':pc,'accessories':accessories,'appliances':appliances})



def cartpayment(request):
    mode=request.POST['mode']
    userid=request.user.id
    if mode=="cod":

        one=Cart.objects.filter(userid=userid,tablename="Tv")
        two=Cart.objects.filter(userid=userid,tablename="Mobiles")
        three=Cart.objects.filter(userid=userid,tablename="Pc")
        four=Cart.objects.filter(userid=userid,tablename="Accessories")
        five=Cart.objects.filter(userid=userid,tablename="Appliances")

    
       
        tv=Tv.objects.filter(id__in=[f.productid for f in one],stock__gte=1)
        mobiles=Mobiles.objects.filter(id__in=[f.productid for f in two],stock__gte=1)
        pc=Pc.objects.filter(id__in=[f.productid for f in three],stock__gte=1)
        accessories=Accessories.objects.filter(id__in=[f.productid for f in four],stock__gte=1)
        appliances=Appliances.objects.filter(id__in=[f.productid for f in five],stock__gte=1)
       
        x=str(time.ctime())
        j=1
        for tv1 in tv:
           j=0
           while j<=10:
               tracking=random.randint(1,99999999)
               if Order.objects.filter(tracking=tracking).exists():
                   print("exists")
               else:
                   break
           o=Order(userid=userid,tablename="TV",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="cod")
           o.save()
           tv1.stock=tv1.stock-1
           tv1.save()


        for tv1 in mobiles:
           j=0
           while j<=10:
               tracking=random.randint(1,99999999)
               if Order.objects.filter(tracking=tracking).exists():
                   print("exists")
               else:
                   break
           o=Order(userid=userid,tablename="MOBILES",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="cod")
           o.save()
           tv1.stock=tv1.stock-1
           tv1.save()

        
        for tv1 in pc:
           j=0
           while j<=10:
               tracking=random.randint(1,99999999)
               if Order.objects.filter(tracking=tracking).exists():
                   print("exists")
               else:
                   break
           o=Order(userid=userid,tablename="PC",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="cod")
           o.save()
           tv1.stock=tv1.stock-1
           tv1.save()


        for tv1 in accessories:
           j=0
           while j<=10:
               tracking=random.randint(1,99999999)
               if Order.objects.filter(tracking=tracking).exists():
                   print("exists")
               else:
                   break
           o=Order(userid=userid,tablename="ACCESSORIES",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="cod")
           o.save()
           tv1.stock=tv1.stock-1
           tv1.save()


        for tv1 in appliances:
           j=0
           while j<=10:
               tracking=random.randint(1,99999999)
               if Order.objects.filter(tracking=tracking).exists():
                   print("exists")
               else:
                   break
           o=Order(userid=userid,tablename="APPLIANCES",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="cod")
           o.save()
           tv1.stock=tv1.stock-1
           tv1.save()
        Cart.objects.filter(userid=userid).delete()
        
        return render(request,'success.html')
    
    else:
        return render(request,'cartonlinepay.html')


def cartonlinepay(request):
    userid=request.user.id

    one=Cart.objects.filter(userid=userid,tablename="Tv")
    two=Cart.objects.filter(userid=userid,tablename="Mobiles")
    three=Cart.objects.filter(userid=userid,tablename="Pc")
    four=Cart.objects.filter(userid=userid,tablename="Accessories")
    five=Cart.objects.filter(userid=userid,tablename="Appliances")

    
       
    tv=Tv.objects.filter(id__in=[f.productid for f in one],stock__gte=1)
    mobiles=Mobiles.objects.filter(id__in=[f.productid for f in two],stock__gte=1)
    pc=Pc.objects.filter(id__in=[f.productid for f in three],stock__gte=1)
    accessories=Accessories.objects.filter(id__in=[f.productid for f in four],stock__gte=1)
    appliances=Appliances.objects.filter(id__in=[f.productid for f in five],stock__gte=1)
       
    x=str(time.ctime())
    j=1
    for tv1 in tv:
        j=0
        while j<=10:
            tracking=random.randint(1,99999999)
            if Order.objects.filter(tracking=tracking).exists():
                print("exists")
            else:
                break
        o=Order(userid=userid,tablename="TV",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="op")
        o.save()
        tv1.stock=tv1.stock-1
        tv1.save()


    for tv1 in mobiles:
        j=0
        while j<=10:
            tracking=random.randint(1,99999999)
            if Order.objects.filter(tracking=tracking).exists():
                print("exists")
            else:
                break
        o=Order(userid=userid,tablename="MOBILES",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="op")
        o.save()
        tv1.stock=tv1.stock-1
        tv1.save()

        
    for tv1 in pc:
        j=0
        while j<=10:
            tracking=random.randint(1,99999999)
            if Order.objects.filter(tracking=tracking).exists():
                print("exists")
            else:
                break
        o=Order(userid=userid,tablename="PC",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="op")
        o.save()
        tv1.stock=tv1.stock-1
        tv1.save()


    for tv1 in accessories:
        j=0
        while j<=10:
            tracking=random.randint(1,99999999)
            if Order.objects.filter(tracking=tracking).exists():
                print("exists")
            else:
                break
        o=Order(userid=userid,tablename="ACCESSORIES",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="op")
        o.save()
        tv1.stock=tv1.stock-1
        tv1.save()


    for tv1 in appliances:
        j=0
        while j<=10:
            tracking=random.randint(1,99999999)
            if Order.objects.filter(tracking=tracking).exists():
                print("exists")
            else:
                break
        o=Order(userid=userid,tablename="APPLIANCES",name=tv1.name,productid=tv1.id,tracking=tracking,status="ordered",times=x,payment="op")
        o.save()
        tv1.stock=tv1.stock-1
        tv1.save()
    Cart.objects.filter(userid=userid).delete()
        
    return render(request,'success.html')



def myorders(request):
    userid=request.user.id
    order=Order.objects.filter(userid=userid)


    return render(request,'myorders.html',{'order':order})