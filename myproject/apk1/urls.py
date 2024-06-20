from django.urls import path
from . import views
from .controller import authview
from django.conf import settings
from django.conf.urls.static import static
from apk1.controller import cart

urlpatterns = [
    path('main.html', views.say_hello),
    path('register.html', authview.register, name='register'),
    path('collections.html',views.collections, name='collections'),
    path('collections/<str:slug>',views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
    path('add-to-cart',cart.addtocart, name='addtocart'),
    path('login', authview.loginpage, name="loginpage"),
    path('logout', authview.logoutpage, name="logout"),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

