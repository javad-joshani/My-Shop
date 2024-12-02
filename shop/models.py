from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User ,auto_now= True )
    phone = models.CharField(max_length=15)
    nationalـcode = models.CharField(max_length=10,blank=True)
    country = models.CharField(max_length=50 ,default="Iran" ,blank=True)
    state = models.CharField(max_length=50 , blank=True)
    city = models.CharField(max_length=50 , blank=True)
    address = models.CharField(max_length=250 , blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender , instance , created ,**kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
post_save.connect(create_profile,sender=User)


class Product(models.Model):
    name =models.CharField(max_length=30)
    description = models.CharField(max_length=300 ,default='',blank=True,null=True)
    price = models.DecimalField(default=0,max_digits=12, decimal_places=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    count_sold = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to="products")
    star = models.IntegerField(default=0 ,validators=[MinValueValidator(0),MaxValueValidator(5)])
    is_special = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name
    
    def get_total_price(self):
        discount_price = self.price * self.discount / 100
        total = self.price - discount_price
        return total
    

class Order(models.Model): #  sefaresh
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='',blank=True,null=True,max_length=200)  # for easy now blank=True
    phone = models.CharField(max_length=15,blank=True)
    date = models.DateTimeField(default=datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.status

class Slider(models.Model):
    title = models.CharField(max_length=55,verbose_name=_("title"))
    image = models.ImageField(upload_to='sliders',verbose_name=_("image"))
    link = models.URLField()
    order = models.PositiveIntegerField(null=True,blank=True,unique=True,verbose_name=_("order"))
    
    class Meta:
        verbose_name = "slide"
        verbose_name_plural = "sliders"
        ordering = ['order']
        
    def save(self,*args,**kwargs):
        if self.order == None:
            last = self.__class__.objects.last()
            self.order = last.order + 1

        super().save(*args,**kwargs)