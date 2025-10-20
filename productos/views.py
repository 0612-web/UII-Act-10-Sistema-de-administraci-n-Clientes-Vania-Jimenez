from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

def index(request):
    return render(request, 'productos/index.html', {
        'productos': Producto.objects.all()
    })

def view_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return redirect('index')

def add(request):
    success = False
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ProductoForm()
    else:
        form = ProductoForm()
    return render(request, 'productos/add.html', {
        'form': form,
        'success': success
    })

def edit(request, id):
    producto = get_object_or_404(Producto, pk=id)
    success = False
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/edit.html', {
        'form': form,
        'success': success
    })

def borrar(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return HttpResponseRedirect(reverse('index'))
