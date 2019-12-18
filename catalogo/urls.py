from django.urls import path
from .views import index, RegistroUsuario, clientecrear,clientelist,ordencrear,success
from . import views

app_name="apps"
urlpatterns = [
    path('', index,name='index'),
	path('clientenew/', clientecrear,name='nuevocliente'),
	path('clientelist',clientelist,name='listacliente'),
	path('registrar/', RegistroUsuario.as_view(),name='registrar'),
	path('crearorden/',ordencrear,name='crearorden'),
	path('success/', success, name='success'),
	path(r'^delete/(?P<pk>\d+)/$', views.DeleteCliente.as_view(), name='delete'),
	path('ingreso/', views.ingreso, name='ingreso'),
]