from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('page/<int:page>/', views.home ,name='home'),
    path('about/', views.about ,name ='about'),
    path('login/', views.login_user ,name ='login'),
    path('logout/', views.logout_user ,name ='logout'),
    path('signup/', views.signup_user ,name ='signup'),
    path('update_user/', views.update_user ,name ='update_user'),
    path('update_password/', views.update_password ,name ='update_password'),
    path('product/<int:pk>', views.single_product ,name ='product'),
    path('last_product/', views.last_product ,name ='last_product'),
    path('category/<str:cat>', views.category ,name ='category'),
    path('category/', views.category_summery ,name ='category_summery'),
    path('search/', views.search ,name ='search'),
    path('bestseller/', views.bestseller ,name ='bestseller'),
    path('favorite_product/', views.favorite_product ,name ='favorite_product'),
]