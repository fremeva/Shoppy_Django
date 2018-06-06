from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from products.forms import ProductForm
from .models import Products


# Create your views here.
class ProductList(ListView):
    model = Products


class ProductDetail(DetailView):
    model = Products

@login_required()
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #product.save()
            return redirect('/')

    return render(request, 'products/create.html', {'form': ProductForm()})


def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if action == 'signup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    return render(request, 'login/login.html', None)




# def index(request):
#     products = Products.objects.order_by('id')
#     context = {
#         'products': products
#     }
#     return render(request, 'products/products_list.html', context)
#
#
# def detail(request, pk):
#     product = get_object_or_404(Products, pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'products/detail.html', context)
