from django.shortcuts import render,redirect
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from food_app.models import *
from restarent_app.models import  *
# Create your views here.

def index(request):
    return render(request, 'food/index.html')

def explore(request):
    return render(request, 'food/explore.html')

def signup(request):
    return render(request, 'food/signup.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        error=False
        if request.method=="POST":
            dic=request.POST
            usr=dic['user']
            email=dic['email']
            print('email=',email)
            pwd=dic['password']
            i = request.FILES['image']
            phone = dic['mobile']
            userdata = User.objects.filter(username=usr)

            if not userdata:
                user = User.objects.create_user(username=usr, email=email, password=pwd)
                Userdeatils.objects.create(user=user, phone=phone, image=i,)
                return redirect('user_login')
            else:
                error = True
    return render(request, 'food/user_register.html', {'error':error})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        error=False
        if request.method=="POST":
            dic=request.POST
            uiser=dic['user']
            passw=dic['password']
            user=authenticate(username=uiser,password=passw)
            if user:
                 login(request,user)
                 return redirect('index')

            else:
             error=True
    return render(request, 'food/user_login.html', {'error':error})

def logoutt(request):
    logout(request)
    return redirect('index')

def admin(request):
    return render(request, "food/admin.html")


def profile(request):
    res=Userdeatils.objects.filter(user=request.user)


    return render(request, 'food/profile.html', {'res':res})


def portfolio(request):

    return render(request,'food/portfolio.html')