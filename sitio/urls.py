from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/',include('catalogo.urls',namespace='catalogo')),
    url(r'', include('catalogo.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]