from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Users
from django.core.mail import send_mail
import random
import datetime
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myuser.models import Order
# Create your views here.



def login(request):
    if request.method=='POST':
        email= request.POST['email']
        passw= request.POST['passw']
        user = auth.authenticate(username=email, password=passw)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'invalid credientials')
            return redirect("/")
    else:
        return render(request,'login.html')
  
    

def register(request):
    return render(request, 'register.html')


    

          
       

def otpgenerate(request):
    if request.method=='GET':
        print("ji")
        email= request.GET['email']
        phone= request.GET['phone']
        first_name= request.GET['first_name']
        print("hi")
        if Users.objects.filter(phone=phone).exists() and Users.objects.filter(email=email).exists() :
            return HttpResponse("Phone Number And Email Already Exists")
        elif Users.objects.filter(phone=phone).exists():
            return HttpResponse("Phone Number Already Exists")
        elif Users.objects.filter(email=email).exists():
            return HttpResponse("Email Already Exists")
        else:
            a=random.randrange(1, 10000)
            b="HI {0},Your OTP For Account Creation is {1}"
            send_mail('Electro-Mark',
            b.format(first_name,a),
            'sanjayvembu20@gmail.com',
            [email],
            fail_silently=False)
            return HttpResponse(a)


def accountcreate(request):
    
     email=request.POST['email']
     phone= request.POST['phone']
     first_name=request.POST['first_name']
     last_name= request.POST['last_name']
     gender= request.POST['gender']
     passw= request.POST['passw']
     birthday=request.POST['birthday']
     father=request.POST['father']
     add1=request.POST['add1']
     add2=request.POST['add2']
     landmark=request.POST['landmark']
     district=request.POST['district']
     pincode=request.POST['pincode']
     
     print("againagainaigainkkkkkkkkkkkkkkkkkkkkk")
     p=Users(first_name=first_name,last_name=last_name,gender=gender,birthday=birthday,email=email,phone=phone,passw=passw,father_name=father,address1=add1,address2=add2,landmark=landmark,district=district,pincode=pincode)
     p.save()
     obj = Users.objects.latest('id')
     mail=obj.email
     pwd=obj.passw
     idd=str(obj.id)

     user = User.objects.create_user(username=mail, password=pwd,first_name=idd)
     user.save()
     
     return redirect("/")


def forgot(request):
    return render(request,'forgot.html')

def forgototp(request):
    if request.method=='GET':
        
        email= request.GET['email']
        
        
        if Users.objects.filter(email=email).exists():
            name=Users.objects.get(email=email)
            first_name=name.first_name
            a=random.randrange(1, 10000)
            b="HI {0},Your OTP For FORGOT PASSWORD is {1}"
            send_mail('Electro-Mark',
            b.format(first_name,a),
            'sanjayvembu20@gmail.com',
            [email],
            fail_silently=False)
            return HttpResponse(a)
        else:
            return HttpResponse("nosend")

def pwdchange(request):
    if request.method=='POST':
        email= request.POST['email']
        passw= request.POST['passw']
        a=email+passw
        u=Users.objects.get(email=email)
        u.passw=passw
        u.save()

        u1=User.objects.get(username__exact=email)
        u1.set_password(passw)
        u1.save()
        return HttpResponse(a)

def editprofile(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        birthday= request.POST['birthday']
        gender= request.POST['gender']
        father_name= request.POST['father']
        address1= request.POST['add1']
        address2= request.POST['add2']
        landmark= request.POST['landmark']
        pincode= request.POST['pincode']
        district= request.POST['district']
        
        b=int(request.user.first_name)
        update=Users.objects.get(id=b)
        update.first_name=first_name
        update.last_name=last_name
        update.birthday=birthday
        update.gender=gender
        update.father_name=father_name
        update.address1=address1
        update.address2=address2
        update.landmark=landmark
        update.pincode=pincode
        update.district=district
        update.save()
        return HttpResponse("ji")
    else:
        a=request.user.first_name
        a=int(a)
        account=Users.objects.get(id=a)
        return render(request,'editprofile.html',{'account':account})



        

def logout(request):
    auth.logout(request)
    return redirect('/')

def updatelocation(request):
    return render(request,'updatelocation.html')

def checktracking(request):
    if request.method=='GET':
        tracking=request.GET['tracking']
        status= request.GET['status']
        if tracking=="":
            return HttpResponse("TRACKING ID IS EMPTY")
        if status != "0":
            if Order.objects.filter(tracking=tracking).exists():
                order=Order.objects.get(tracking=tracking)
                order.status=status
                order.save()
                return HttpResponse("SUCCESSFULLY STATUS OF THE PRODUCT IS UPDATED")
            else:
                return HttpResponse("ENTER CORRECT TRACKING ID")
        else:
            return HttpResponse("CHOOSE STATUS OF THE PRODUCTS")

        