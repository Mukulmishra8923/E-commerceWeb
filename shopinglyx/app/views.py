from django.shortcuts import render,redirect
from django.views import View
from . models import Costumer,Product,OrderPlaced,cart,profile_i
from .forms import customerRegistrationForm,LoginForm,PasswordChangeForm,CustomerProfileForm,profile_imgForm
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# def home(request):
#  return render(request, 'app/home.html')

class productview(View):
 def get(self, request):
  Topwears = Product.objects.filter(category='TW')
  Bottamwears = Product.objects.filter(category='BW')
  Laptops = Product.objects.filter(category='L')
  Mobiles = Product.objects.filter(category='M')
  return render(request,'app/home.html',{'Topwears':Topwears,'Bottamwears':Bottamwears,'Laptops':Laptops,'Mobiles':Mobiles})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')



class productdetailview(View):
   def get(self,request, pk):
    product=Product.objects.get(pk=pk)
    item_already_in_cart = False

    if request.user.is_authenticated:
     item_already_in_cart=cart.objects.filter(Q(product=product.id)& 
       Q(user=request.user)).exists()

    return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})
   
  

 
@login_required
def add_to_cart(request):
 user=request.user
 product_id=request.GET.get('prod_id')
 product=Product.objects.get(id=product_id)
 cart(user=user, product=product).save()
 return redirect('/show_cart')

@login_required
def show_cart(request):
   if request.user.is_authenticated:
      user=request.user
      Cart=cart.objects.filter(user=user)
      amount=0.0
      shipping_amount=40.0
      total_amount=0.0
      cart_product=[p for p in cart.objects.all() if p.user==user ]

      if cart_product:
        for p in cart_product:
         tempamount=(p.quantity* p.product.discounted_price)
         amount +=tempamount
         total_amount=amount+shipping_amount
        return render(request,'app/addtocart.html', 
        {'carts':Cart,'totalamount':total_amount ,'amount':amount}) 
      else:
       return render(request,'app/emptycart.html')
      
def pluscart(request):
 if request.method == 'GET':
     prod_id = request.GET['prod_id']
     print('pid',prod_id)
     c = cart.objects.get(Q(product=prod_id) & Q(user= request.user))
      
     print('cd is',c)
     c.quantity+=1
     c.save()
     print(c.quantity)
     amount=0.0
     shipping_amount=40.0
     total_amount=0.0
     cart_product=[p for p in cart.objects.all() if p.user == request.user ]

  
     for p in cart_product:
        tempamount=(p.quantity* p.product.discounted_price)
        amount +=tempamount
        total_amount=amount+shipping_amount

     data={
           'quantity':c.quantity,
           'amount' :amount,
           'totalamount':total_amount
       }
       
     print('data is ',data)
     return JsonResponse(data)  
    
   

def minuscart(request):
  if request.method == 'GET':
     prod_id = request.GET['prod_id']
     print('pid',prod_id)
     c = cart.objects.get(Q(product=prod_id) & Q(user= request.user))
      
     print('cd is',c)
     c.quantity+=1
     c.save()
     print(c.quantity)
     amount=0.0
     shipping_amount=40.0
     total_amount=0.0
     cart_product=[p for p in cart.objects.all() if p.user == request.user ]

  
     for p in cart_product:
        tempamount=(p.quantity* p.product.discounted_price)
        amount -=tempamount
        total_amount=amount+shipping_amount

     data={
           'quantity':c.quantity,
           'amount' :amount,
           'totalamount':total_amount
       }
       
     print('data is ',data)
     return JsonResponse(data)  



def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

def address(request):
 add=Costumer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})


@login_required
def orders(request):
 user=request.user
 op=OrderPlaced.objects.filter(user=user)
 return render(request, 'app/orders.html',{'order_placed':op})


def passwordchangedone(request):
 return render(request,'app/passwordchangedone.html')





def mobile(request, data=None):
 if data ==None:
   Mobiles = Product.objects.filter(category='M')
 elif data =='Samsung' or data =='Xiaomi' or data =='Tecno' or data =='realme' or data =='Apple' :
   Mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data =='below':
  Mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=100000) 
 elif data =='above':
  Mobiles =Product.objects.filter(category='M').filter(discounted_price__gt=100000) 

  
 return render(request, 'app/mobile.html',{'mobiles':Mobiles})

 


def laptop(request, data=None):
 if data ==None:
   laptop = Product.objects.filter(category='L')
 elif data =='Samsung' or data =='Xiaomi' or data =='dell' or data =='Asus' or data =='Apple' or data =='HP' or data =='Lenovo':
   laptop = Product.objects.filter(category='L').filter(brand=data)
 elif data =='below':
  laptop =Product.objects.filter(category='L').filter(discounted_price__lt=60000) 
 elif data =='above':
  laptop =Product.objects.filter(category='L').filter(discounted_price__gt=60000) 

 return render(request, 'app/laptop.html',{'laptop':laptop})

def topwear(request, data=None):
 if data ==None:
   topwear = Product.objects.filter(category='TW')
 elif data =='below':
  topwear =Product.objects.filter(category='TW').filter(discounted_price__lt=1300) 
 elif data =='above':
  topwear =Product.objects.filter(category='TW').filter(discounted_price__gt=1300) 

 return render(request, 'app/topwear.html',{'topwear':topwear})

def bottamwear(request, data=None):
 if data ==None:
   bottamwear = Product.objects.filter(category='BW')
 elif data =='below':
  bottamwear =Product.objects.filter(category='BW').filter(discounted_price__lt=800) 
 elif data =='above':
  bottamwear =Product.objects.filter(category='BW').filter(discounted_price__gt=800) 

 return render(request, 'app/bottamwear.html',{'bottamwear':bottamwear})

# def login(request):
#   lm=LoginForm() 
#   return render(request, 'app/login.html',{'form':lm})


class customerRegistrationView(View):
 def get(self ,request):
  form=customerRegistrationForm()
  return render(request,'app/customerregistration.html',{'form':form})
 def post(self, request):
  form=customerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations !! Registred Successfully')
   form.save()
   
  return render(request,'app/customerregistration.html',{'form':form})
 


def checkout(request):
 user=request.user
 add=Costumer.objects.filter(user=user)
 cart_items=cart.objects.filter(user=user)
 amount=0.0
 shipping_amount=40.0
 cart_product=[p for p in cart.objects.all() if p.user == user ]
 if cart_product:
        for p in cart_product:
         tempamount=(p.quantity* p.product.discounted_price)
         amount +=tempamount
         total_amount=amount+shipping_amount

 return render(request, 'app/checkout.html',{'add':add,'totalamount':total_amount ,'cart_items':cart_items})

@login_required
def paymentdone(request):
  user= request.user
  custid=request.GET.get('custid')
  customer=Costumer.objects.get(id=custid)
  Cart =cart.objects.filter(user=user)

  for c in Cart:
    OrderPlaced(user=user, costumer=customer, product=c.product , quantity=c.quantity ).save()
    c.delete()
  return redirect("orders")

@method_decorator(login_required ,name='dispatch')
class ProfileView(View):
 def get(self,request):
  form=CustomerProfileForm()
  return render(request,'app/profile.html',{'form':form}) 
 def post(self,request):
   form=CustomerProfileForm(request.POST)
   if form.is_valid():
    user=request.user
    name=form.cleaned_data['name']
    locality=form.cleaned_data['locality']
    city=form.cleaned_data['city']
    state=form.cleaned_data['state']
    zipcode=form.cleaned_data['zipcode']
    reg= Costumer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
    reg.save()
    messages.success(request,'congratulation!! your profile updated successfully')
    return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})


def profile_imgView(request):
  # if request.method =='POST':
  #   fm=profile_imgForm(request.POST, request.FILES)
  #   if fm.is_valid():
  #      fm.save()
  #      img_obj = fm.instance
  
  #   return render(request,'app/profile_pic.html',{'form':fm,'active':
  #                 'btn- primary','img_obj':img_obj})
  # else:
  #   fm=profile_imgForm()
  # return render(request,'app/profile_pic.html',{'form':fm,'active':
  #                 'btn- primary'})
    fmm=profile_imgForm()
    fm=profile_i.objects.all()
    print(fm)
    return render(request,'app/profile_pic.html',{'fm':fm,'fmm':fmm})


def search(request):
  query=request.GET['query']
  ser =Product.objects.filter(title__icontains=query)
  print(ser)
  return render(request,'app/search.html',{"ser":ser})


# def profile_im(request):
#   form = profile_i.objects.all()
#   print(form)
#   return render(request,'app/profile_pic.html',{'form':form})
