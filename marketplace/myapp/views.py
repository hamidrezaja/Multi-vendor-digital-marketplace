from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'myapp/index.html',{'products':products})
def detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'myapp/detail.html',{'product':product})
def create_product(request):
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('index')
    product_form=ProductForm()
    return render(request,'myapp/create_product.html',{'product_form':product_form})