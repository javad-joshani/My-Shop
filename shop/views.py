from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.db.models import Q
from django.utils.translation import activate
from django.core.paginator import Paginator

from .forms import SignupForm,UpdateUserForm,UpdatePasswordForm
from .models import Category,Customer,Profile,Product,Order,Slider

from rest_framework import viewsets,permissions 
from .serializers import CategorySerializer,CustomerSerializer,ProfileSerializer,ProductSerializer,OrderSerializer,SliderSerializer
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

# Create your views here.



def home(request,page=1):
    products = Product.objects.all()
    slides = Slider.objects.all()
    paginator  = Paginator(products,4)
    products = paginator.get_page(page)
    context ={
       "products":products,
       "slides":slides,
    }
    return render(request,"index.html",context)


def about(request):
    return render(request , "about.html")


def login_user(request):
   if request.method == "POST":
      username = request.POST['username']  
      password = request.POST['password']  
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request,user)
         messages.success(request,("با موفقیت وارد شدید !"))
         return redirect("home")
      else:
         messages.success(request,("مشکلی در لاگین وجود داشت"))
         return redirect("login")

   else:
      return render(request , "auth/login.html")
   

def logout_user(request):
    logout(request)
    messages.success(request , ("با موفقیت خارج شدید !"))
    return redirect("home")



def signup_user(request):
   form = SignupForm()
   if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         password1 = form.cleaned_data['password1']
         user = authenticate(request,username=username ,password=password1)
         login(request,user)
         messages.success(request , ("ثبت نام با موفقیت انجام شد"))
         return redirect("home")
      else:
         print(form.errors)
         messages.success(request , ("ثبت نام انجام نشد !!"))
         return render(request,"auth/signup.html" ,{"form":form})

   else:
      return render(request,"auth/signup.html" ,{"form":form})
   

   
def update_user(request):
   if request.user.is_authenticated:
      user = User.objects.get(id=request.user.id)
      form = UpdateUserForm(request.POST or None, instance = user)

      if form.is_valid():
         form.save()
         login(request , user)
         messages.success(request ,"ویرایش انجام شد !")
         return redirect("home")
      else:
         return render(request , "auth/update_user.html",{"form":form})
   else:
      messages.success(request , "ابتدا لاگین کنید")
      return redirect("login")
   
   
def update_password(request):
   if request.user.is_authenticated:
      user = request.user

      if request.method =='POST':
         form = UpdatePasswordForm(user,request.POST)
         if form.is_valid():
            form.save()
            messages.success(request ,"رمز شما با موفقیت تغییر کرد !")
            login(request ,user)
            return redirect('home')
         else:
            messages.success(request ,"فرم معتبر نیست !!")
            form = UpdatePasswordForm(user)
         return render(request , "auth/update_password.html",{"form":form})

      else:
         form = UpdatePasswordForm(user)
         return render(request , "auth/update_password.html",{"form":form})
   else:
      messages.success(request ,"ابتدا به حساب خود وارد شوید !")
      return redirect('login')
   

def single_product(request,pk):
   product = Product.objects.get(id=pk)
   return render(request , "single_product.html",{"product":product})



def last_product(request):
   last_product = Product.objects.order_by("created")
   return render(request , "last_product.html",{"last_product":last_product})

def bestseller(request):
   bestseller = Product.objects.order_by("-count_sold")
   return render(request , "bestseller.html",{"bestseller":bestseller})

def favorite_product(request):
   favorite_product = Product.objects.filter(is_special=True)
   return render(request , "favorite_product.html",{"favorite_product":favorite_product})


def category(request,cat):
   cat = cat.replace("-"," ")
   try:
      category= Category.objects.get(name=cat)
      products = Product.objects.filter(category=category)
      context={
         "category":category,
         "products":products,
      }
      return render(request , 'category.html' ,context)
   except:
      messages.success(request , ("دسته بندی وجود ندارد"))
      return redirect('home')



def category_summery(request):
    category = Category.objects.all()
    context ={
      "category":category
    }
    return render(request,"category_summery.html",context)


def search(request):
   if request.method == "POST":
      searched = request.POST['searched']
      searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
      
      if not searched:
         messages.success(request , "محصولی برای این جستجو یافت نشد !!")
         return redirect("home")
      else:
         return render(request,"search.html",{"searched":searched})
   
   return render(request,"search.html",{})



# ---------------------------------API----------------------------------------


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class ProductPagination(PageNumberPagination):
    page_size = 6

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def perform_create(self, serializer):
        serializer.save()


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SliderViewSet(viewsets.ModelViewSet):

    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ['name', 'description']

class ProductSearchViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset