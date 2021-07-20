from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView

from restarent_app.models import *
from food_app.models import *
from restarent_app.forms import *
from django.contrib import messages
from django.views import View
# Create your views here.

def restarent_register(request):
    if request.user.is_authenticated:
        return redirect("index")

    else:
        error = False

        if request.method == "POST":
            dic = request.POST
            rid = dic['rid']
            runame = dic['rusername']
            rname = dic['rname']
            remail = dic['remail']
            rtype = dic['rtype']
            rpwd = dic['rpassword']
            rimg = request.FILES['rimage']
            raddress = dic['raddress']
            rcity = dic['rcity']
            rststa = dic['rstate']
            rzip = dic['rzip']
            rstatus = 'pending'
            restaurent_data = User.objects.filter(username=runame)
            if not restaurent_data:
                rest_user = User.objects.create_user(username=runame, email=remail, password=rpwd)
                RestaurentModel.objects.create(rest_username=rest_user, rest_name=rname, rest_image=rimg,
                                               rest_status=rstatus,
                                               rest_id=rid, rest_type=rtype, rest_state=rststa,
                                               rest_city=rcity, rest_pincode=rzip, rest_address=raddress)
                return redirect('restarent_login')

            else:
                error = True

    return render(request, 'restaurent/restaurant_register.html', {'error': error})

def restarent_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        error = False

        if request.method == "POST":
            dic = request.POST
            ruiser = dic['ruser']
            rpassw = dic['rpassword']
            user = authenticate(username=ruiser, password=rpassw)

            if user:
                login(request, user)
                return redirect('index')

            else:
                error = True

    return render(request, 'restaurent/restaurant_login.html', {'error': error})

def restaurent_dashboard(request):
        restaurent=RestaurentModel.objects.filter(rest_name=request.user)
        data=OredrModel.objects.filter(usr=request.user).order_by('-created_at')
        count = OredrModel.objects.filter(usr=request.user).count()
        res=Userdeatils.objects.filter(user=request.user)

        return render(request, 'restaurent/user_dashboard.html',
                      {'data':data,'res':res,'count':count,'model':restaurent  })

def admin(request):
    return render(request, 'food/admin.html')

def add_food(request, pk):
    usr = request.user
    rest = RestaurentModel.objects.get(rest_id=pk)
    print(rest.rest_name)
    print(rest.rest_status)
    if rest.rest_status == "Approved" or rest.rest_status == "approved":
        return render(request, 'restaurent/addfood.html',
                      {'model': RestaurentModel.objects.filter(rest_name=request.user)})

    else:
        return render(request, 'restaurent/user_dashboard.html',
                      {
                          'error': 'Soory..! your restaurent has not confirmed with admin till now , please contact to admin department for approved',
                          'model': RestaurentModel.objects.filter(rest_name=request.user)
                          })

def rest_view_food(request,pk):
    rest = AddFoodModel.objects.filter(rname=pk)
    return render(request,'restaurent/restaurent_view_food.html',{'res':rest})


def add_dish(request):
    rname=request.POST['rname']
    did=request.POST['did']
    dname=request.POST['dname']
    dcat=request.POST['dcat']
    dtype=request.POST['dtype']
    dprivce=request.POST['dprice']
    img1=request.FILES['image1']
    img2=request.FILES['image2']
    img3=request.FILES['image3']

    AddFoodModel.objects.create(rname=rname,fid=did,dname=dname,
                                dprice=dprivce,dcat=dcat,dtype=dtype,
                                image1=img1,image2=img2,image3=img3)
    return redirect('user_dashboard')



@login_required(login_url='signup')

def restaurents(request):
    res = RestaurentModel.objects.filter(rest_status='approved')
    return render(request, 'restaurent/restaurents.html', {'res': res})

def view_food(request, pk):

    rest = AddFoodModel.objects.filter(rname=pk)

    rname = request.GET.get('rname')
    type = request.GET.get('type')
    city = request.GET.get('city')

    restro=RestaurentModel.objects.get(rest_name=rname)
    rimg=restro.rest_image.url


    address = request.GET.get('address')
    return render(request, 'restaurent/view_food.html', {'res': rest, 'rname': rname,
                                                         'type': type, 'address': address,
                                                         'city': city,'rimg':rimg} )

# def add_to_cart(request,pk):
#    data=AddFoodModel.objects.filter(fid=pk).first()
#    print(data.fid)
#    print(data.rname)
#    print(data.dname)
#    print(data.dtype)
#   return render(request)

class Add_to_cart(View):
    def post(self, request, pk):
        data = AddFoodModel.objects.get(fid=pk)
        prodta = AddtocartModel.objects.filter(usr=request.user, pro=data).first()

        if prodta:
            messages.error(request, 'sorry this Item is already added to the cart ')
            return render(request, 'restaurent/view_food.html')
        else:
            AddtocartModel.objects.create(usr=request.user, pro=data)
            return redirect('view_cart')

class View_cart(View):
    def get(self, request):
        data = AddtocartModel.objects.filter(usr=request.user).order_by('-created_at')
        return render(request, 'restaurent/view_cart.html', {'data': data, })

class Order_cart(View):


    def post(self, request, pk):
        prodata = AddtocartModel.objects.get(pro__fid=pk,usr=request.user)
        dic = request.POST
        qty = dic['quantity']

        print(prodata.pro.fid)
        total = prodata.pro.dprice * int(qty) + 20
        return render(request, 'restaurent/order.html',
                      {'dimg': prodata.pro.image1.url,
                       'dname': prodata.pro.dname, 'qty': qty,
                       'total': total, 'rname': prodata.pro.rname,
                       'oid': prodata.pro.fid,
                       })

def order_item(request):
    oid = request.GET.get('oid')
    qty = request.GET.get('qty')
    price = request.GET.get('price')
    del_name = request.POST.get('del_name')
    del_address = request.POST.get('del_address')
    del_mobile = request.POST.get('del_mobile')

    pro = AddtocartModel.objects.filter(pro__fid=oid , usr=request.user).first()
    OredrModel.objects.create(usr=request.user, fullname=del_name, oid=oid,
                              rname=pro.pro.rname, dname=pro.pro.dname, dcat=pro.pro.dcat,
                              address1=del_address, quantity=qty, mobile=del_mobile,
                              payment_status='not_done', order_status='confirmed', amount=price)
    AddtocartModel.objects.get  (pro__fid=oid,usr=request.user).delete()
    return redirect('user_dashboard')

class Delete_cart(View):
    def post(self,request,pk):
         AddtocartModel.objects.filter(pro__fid=pk).delete()
         return redirect('view_cart')


class View_promos(View):
      def get(self,request):
          proms=PromosModel.objects.all()
          return render(request,'restaurent/promos.html',{'promo':proms})


def veg(request):
    res=AddFoodModel.objects.filter(dtype='veg')
    return render(request,'restaurent/veg.html',{'res':res})


def non_veg(request):
    res = AddFoodModel.objects.filter(dtype='non-veg')
    return render(request, 'restaurent/non_veg.html', {'res': res})


def chicken(request):
    res = AddFoodModel.objects.filter(dcat='chicken'  )
    return render(request, 'restaurent/chicken.html', {'res': res})


def muttun(request):
    res = AddFoodModel.objects.filter(dcat='mutton')
    return render(request, 'restaurent/mutton.html', {'res': res})


def fish(request):
    res = AddFoodModel.objects.filter(dcat='fish')
    return render(request, 'restaurent/fish.html', {'res': res})


def crabs(request):
    res = AddFoodModel.objects.filter(dcat='crabs')
    return render(request, 'restaurent/crabs.html', {'res': res})


def prawns(request):
    res = AddFoodModel.objects.filter(dcat='prawns')
    return render(request, 'restaurent/prawns.html', {'res': res})


def ice(request):
    res = AddFoodModel.objects.filter(dcat='ice')
    return render(request, 'restaurent/ice.html', {'res': res})


def colas(request):
    res = AddFoodModel.objects.filter(dtype='drinks')
    return render(request, 'restaurent/colas.html', {'res': res})


def pizza(request):
    res = AddFoodModel.objects.filter(dcat='pizza')
    return render(request, 'restaurent/pizzas.html', {'res': res})


def edit_food(request,pk):
    data=AddFoodModel.objects.get(fid=pk)



    return render(request,'restaurent/edit_restaurent.html',{'fid':data.fid,'dname':data.dname,'dprice':data.dprice,
             'dtype':data.dtype,'dcat':data.dcat})


def save_rest_edit_info(request,pk):
    global fid, dname, dprice, dcat, dtype

    if request.method=="POST":
        fid=request.POST['fid']
        dname=request.POST['dname']
        dprice=request.POST['dprice']
        dcat=request.POST['dcat']
        dtype=request.POST['dtype']
        print(fid)
        print()
    data=AddFoodModel.objects.filter(fid=pk)
    data.update(fid=fid,dname=dname,dprice=dprice,dcat=dcat,dtype=dtype)
    return redirect('user_dashboard')


def delete_food(request,pk):
    data = AddFoodModel.objects.filter(fid=pk)
    data.delete()
    return redirect('user_dashboard')


def edit_restaurent_info(request,pk):
    data=RestaurentModel.objects.get(rest_id=pk)

    return render(request,'restaurent/edit_rest_info.html',{'data':data})


def save_rest_info(request,pk):
    global rcity, rtype, rstate, rpin, raddr
    if request.method == "POST":
        rcity = request.POST['rcity']
        rtype = request.POST['rtype']
        raddr= request.POST['raddr']
        rstate = request.POST['rstate']
        rpin = request.POST['rpin']

    data = RestaurentModel.objects.filter(rest_id=pk)
    data.update(rest_city=rcity,rest_type=rtype,rest_state=rstate,rest_pincode=rpin,rest_address=raddr)
    return redirect('user_dashboard')


def delete_restaurent(request,pk):
    data = RestaurentModel.objects.get(rest_id=pk)
    data.delete()
    return redirect('signup')
