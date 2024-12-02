from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms

class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام خود را وارد کنید'}),max_length=30,label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام خانوادگی خود را وارد کنید'}),max_length=30,label="")
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'ایمیل'}),label="")
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام کاربری'}),max_length=30,label="",required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'name':'password1','type':'password','placeholder':' رمز ورود'}),max_length=30,label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'name':'password1','type':'password','placeholder':'تکرار رمز ورود'}),max_length=30,label="")

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')


class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام خود را وارد کنید'}),max_length=30,label="نام :")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام خانوادگی خود را وارد کنید'}),max_length=30,label="نام خانوادگی :")
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام کاربری'}),max_length=30,label="نام کاربری :",required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'شماره تماس'}),max_length=10,label="شماره تماس :",required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'ایمیل'}),label="ایمیل :",required=False)
    nationalـcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'کد ملی'}),max_length=11,label="کد ملی :",required=False)
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'ایران'}),max_length=30,label="کشور :",required=False)
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'استان'}),max_length=30,label="استان :",required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'شهر'}),max_length=30,label="شهر :",required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'ادرس خود را کامل بنویسید'}),max_length=255,label="ادرس :",required=False)


    class Meta:
        model = User
        fields = ('first_name','last_name','username','phone','email','nationalـcode','country','state','city','address')


class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'name':'password1','type':'password','placeholder':' رمز ورود'}),max_length=30,label="")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'name':'password1','type':'password','placeholder':'تکرار رمز ورود'}),max_length=30,label="")
    class Meta:
        model = User
        fields = ['new_password1','new_password2']

