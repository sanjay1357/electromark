from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from myuser.models import Cart
from django.db.models import Q
# Create your views here.

@login_required(login_url='/login/')
def viewproduct(request):
    
    return render(request, 'viewproduct.html')
@login_required(login_url='/login/')
def addproduct(request): 
    return render(request, 'addproduct.html')
@login_required(login_url='/login/')
def home(request):
   mobiles=Mobiles.objects.all().last()
   tv=Tv.objects.all().last()
   pc=Pc.objects.all().last()
   appliances=Appliances.objects.all().last()
   accessories=Accessories.objects.all().last()

   mobiles1=Mobiles.objects.all().first()
   tv1=Tv.objects.all().first()
   pc1=Pc.objects.all().first()
   appliances1=Appliances.objects.all().first()
   accessories1=Accessories.objects.all().first()

   d1 = Mobiles.objects.all().order_by('-discount')[:2]
   d2 = Accessories.objects.all().order_by('-discount')[:2]
   d3 = Tv.objects.all().order_by('-discount')[:2]
   d4 = Pc.objects.all().order_by('-discount')[:2]
   d5 = Appliances.objects.all().order_by('-discount')[:2]


   return render(request,'home.html',{'mobiles':mobiles,'tv':tv,'pc':pc,'appliances':appliances,'accessories':accessories,'mobiles1':mobiles1,'tv1':tv1,'pc1':pc1,'appliances1':appliances1,'accessories1':accessories1,'d1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5})
def adding(request):
    if request.method=='POST':
        category=request.POST['category']
        if category=="MOBILES" or category=="TABLETS":
           form=Mob(request.POST,request.FILES)
           if form.is_valid():
              form.save()
              obj=Mobiles.objects.latest('id')
              obj.discount=(obj.oriprice-obj.curprice)*100
              obj.discount=obj.discount/obj.oriprice
              obj.save()
              return HttpResponse('success')
           else:
               return HttpResponse('nosuccess2')
       
           
        elif category=="COMPUTERS" or category=="LAPTOPS":
           form=Pcform(request.POST,request.FILES)
           if form.is_valid():
              form.save()
              obj=Pc.objects.latest('id')
              obj.discount=(obj.oriprice-obj.curprice)*100
              obj.discount=obj.discount/obj.oriprice
              obj.save()
              return HttpResponse('success')
           else:
               return HttpResponse('nosuccess1')

        elif category=="TV":
           form=Tvform(request.POST,request.FILES)
           if form.is_valid():
              form.save()
              obj=Tv.objects.latest('id')
              obj.discount=(obj.oriprice-obj.curprice)*100
              obj.discount=obj.discount/obj.oriprice
              obj.save()
              return HttpResponse('success')
           else:
               return HttpResponse('nosuccess')

        elif category=="ACCESSORIES":
           form=Accessoriesform(request.POST,request.FILES)
           if form.is_valid():
              form.save()
              obj=Accessories.objects.latest('id')
              obj.acctype=request.POST['acctype']
              obj.accfeatures=request.POST['accfeatures']
              obj.accinterfaces=request.POST['accinterfaces']
              obj.acccapacity=request.POST['acccapacity']
              obj.accconnectivity=request.POST['accconnectivity']
              obj.save()

              obj1=Accessories.objects.latest('id')
              obj1.discount=(obj1.oriprice-obj1.curprice)*100
              obj1.discount=obj1.discount/obj1.oriprice
              obj1.save()
              return HttpResponse('success')
           else:
               return HttpResponse('nosuccess')
           
        elif category=="APPLIANCES":
           form=Appliancesform(request.POST,request.FILES)
           if form.is_valid():
              form.save()
              obj=Appliances.objects.latest('id')
              obj.appsize=request.POST['appsize']
              obj.appfeatures=request.POST['appfeatures']
              obj.save()

              obj1=Appliances.objects.latest('id')
              obj1.discount=(obj1.oriprice-obj1.curprice)*100
              obj1.discount=obj1.discount/obj1.oriprice
              obj1.save()
              return HttpResponse('success')
           else:
               return HttpResponse('nosuccess')
        else:
            return HttpResponse("error occured")
       
        
            
       
       


def productvalidate(request):
    if request.method=='GET':
        print("kkkkkkkkkkkkkkkkkkkkkkkkkk")
        category = request.GET['category']
        name = request.GET['name']
        if category=="MOBILES" or category=="TABLETS":
            ram = request.GET['ram']
            internal = request.GET['internal']
            color = request.GET['color']
            if Mobiles.objects.filter(name=name,ram=ram,internal=internal,color=color).exists():
                return HttpResponse("exists")
            else:
                return HttpResponse("notexists")
        elif category=="COMPUTERS" or category=="LAPTOPS":
            pcram = request.GET['pcram']
            print("llllllllllllllllllll")
            if Pc.objects.filter(name=name,pcram=pcram).exists():
                return HttpResponse("exists")
            else:
                return HttpResponse("notexists")
        
        elif category=="TV":
            if Tv.objects.filter(name=name).exists():
                return HttpResponse("exists")
            else:
                return HttpResponse("notexists")

        elif category=="ACCESSORIES":
            if Accessories.objects.filter(name=name).exists():
                return HttpResponse("exists")
            else:
                return HttpResponse("notexists")

        elif category=="APPLIANCES":
            if Appliances.objects.filter(name=name).exists():
                return HttpResponse("exists")
            else:
                return HttpResponse("notexists")

        
     
def allproduct(request,category):
    if category=="MOBILES":
       one=Mobiles.objects.filter(category=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="TABLETS":
       one=Mobiles.objects.filter(category=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="COMPUTERS":
       one=Pc.objects.filter(category=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="LAPTOPS":
       one=Pc.objects.filter(category=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="TV":
       one=Tv.objects.filter(category=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="EXTERNAL HARD DISKS":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="HEADSETS":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="KEYBOARDS":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="MOBILE CASES":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="MOBILE CHARGERS":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="MOUSE":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="POWER BANKS":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="TEMPERED GLASS":
       one=Accessories.objects.filter(subcategory1=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="AIR CONDITIONERS":
       one=Appliances.objects.filter(subcategory2=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="FANS":
       one=Appliances.objects.filter(subcategory2=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="REFRIGERATORS":
       one=Appliances.objects.filter(subcategory2=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})
    elif category=="WASHING MACHINE":
       one=Appliances.objects.filter(subcategory2=category)
       return render(request, 'allproduct.html',{'mobiles':one,'category':category})

@login_required(login_url='/login/')
def filter(request,category):
    price=request.POST['price']
    rating=request.POST['rating']
    discount=request.POST['discount']
    print("jjjjjjjjjjjjjjjjjjjkk")
    print(category)
    if category=="TV":
        if discount=="1" and price=="1":
           tv=Tv.objects.filter(rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Tv.objects.filter(rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Tv.objects.filter(rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Tv.objects.filter(rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Tv.objects.filter(rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Tv.objects.filter(rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Tv.objects.filter(rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Tv.objects.filter(rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN TV")



    elif category=="MOBILES":
        print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        if discount=="1" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN MOBILES")    
        
    elif category=="TABLETS":
        if discount=="1" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Mobiles.objects.filter(category=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN TABLETS")   


    elif category=="COMPUTERS":
        if discount=="1" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN TABLETS")   
    

    elif category=="LAPTOPS":
        if discount=="1" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Pc.objects.filter(category=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN TABLETS")

    
    elif category=="WASHING MACHINE":
        if discount=="1" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN WM")  


    elif category=="FANS":
        if discount=="1" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN FANS")   


    elif category=="AIR CONDITIONERS":
        if discount=="1" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN AC")   


    elif category=="REFRIGERATORS":
        if discount=="1" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Appliances.objects.filter(subcategory2=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN FRIDGE")   




    elif category=="HEADSETS":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN HS")



    elif category=="MOBILE CASES":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN MC")   



    elif category=="TEMPERED GLASS":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN TG")   


    elif category=="MOBILE CHARGERS":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN MC")           


    elif category=="MOUSE":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')   
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN MOUSE")   


    
    elif category=="POWER BANKS":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN PB")   



    elif category=="EXTERNAL HARD DISKS":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN EHD")   


    
    elif category=="KEYBOARDS":
        if discount=="1" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('curprice')
        elif discount=="1" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__lte=24).order_by('-curprice')
        elif discount=="2" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('curprice')
        elif discount=="2" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=25,discount__lte=50).order_by('-curprice')
           
        elif discount=="3" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('curprice')
        elif discount=="3" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=51,discount__lte=75).order_by('-curprice')
        elif discount=="4" and price=="1":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('curprice')
        elif discount=="4" and price=="2":
           tv=Accessories.objects.filter(subcategory1=category,rating=rating,discount__gte=76).order_by('-curprice')
        else:
            return HttpResponse("ERROR OCCURED DURING FILTER IN EHD")  
   


    else:
        return HttpResponse("over all") 
    return render(request, 'allproduct.html',{'mobiles':tv,'category':category})


@login_required(login_url='/login/')
def description(request,category,id):
   like="error"
   if category=="TV":
      like="TV"
      obj=Tv.objects.get(id=id)
   elif category=="MOBILES" or category=="TABLETS":
      like="MOBILES"
      obj=Mobiles.objects.get(id=id)
   elif category=="COMPUTERS" or category=="LAPTOPS":
      like="PC"
      obj=Pc.objects.get(id=id)
   elif category=="FANS" or category=="AIR CONDITIONERS" or category=="REFRIGERATORS" or category=="WASHING MACHINE":
      like="APPLIANCES"
      obj=Appliances.objects.get(id=id)
   else:
      like="ACCESSORIES"
      obj=Accessories.objects.get(id=id)
  
   return render(request, 'description.html',{'obj':obj,'category':like})
    

def search(request):
   if request.method=='GET':
      category= request.GET['category']
      search=request.GET['search']

      if category=="MOBILES":
         mobiles=Mobiles.objects.filter(Q(name__icontains=search))

      elif category=="PC":
         mobiles=Pc.objects.filter(Q(name__icontains=search))

      elif category=="TV":
         mobiles=Tv.objects.filter(Q(name__icontains=search))

      elif category=="ACCESSORIES":
         mobiles=Accessories.objects.filter(Q(name__icontains=search))

      elif category=="APPLIANCES":
         mobiles=Appliances.objects.filter(Q(name__icontains=search))
      
      else:
         return HttpResponse("error in search func()")

      return render(request,'search.html',{'mobiles':mobiles,'category':category})
   else:
      return HttpResponse("li2")