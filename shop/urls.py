from django.urls import path,include
from . import views
from .views import CategoryViewSet, CustomerViewSet, ProfileViewSet, ProductViewSet, OrderViewSet, SliderViewSet, ProductSearchViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'sliders', SliderViewSet)
router.register(r'search-products', ProductSearchViewSet,basename='product_search')
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
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