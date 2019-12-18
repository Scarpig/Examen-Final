from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClienteForm, OrdenForm
from .models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import RegistroForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def index(request):
	return render(request,"index.html")

def clientecrear(request):
	if request.method =='POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('catalogo:success')
	else:
		form = ClienteForm()

		return render(request,'clienteform.html',{'form':form})

def ingreso(request):
	return render(request,'login.html')

def clientelist(request):
	cliente = Cliente.objects.all()
	contexto = {'clientes':cliente}
	return render(request, 'clientelist.html',contexto)

class RegistroUsuario(CreateView):
	model = User
	template_name = "registro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('catalogo:index')

def ordencrear(request):
	if request.method =='POST':
		form = OrdenForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('catalogo:success')
	else:
		form = OrdenForm()

		return render(request,'ordenform.html',{'form':form})

def success(request):
    return render(request,'success.html')

class DeleteCliente(DeleteView):
	model = Cliente
	template_name = "registro/deletecliente.html"
	# success_url = reverse_lazy('catalogo:listacliente') error aca eliminar 

class UpdateCliente(UpdateView):
	model = Cliente
	fields = ['nombre','direction','ciudad','comuna','telefono','email']
