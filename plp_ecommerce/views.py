from django.shortcuts import get_object_or_404, render
from .models import Product, Customer
#from django.http import HttpResponse
#from django.shortcuts import HttpResponse

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'plp_ecommerce/product_list.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'plp_ecommerce/product_details.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers' : customers
    }
    return render(request, 'plp_ecommerce/customer_list.html', context)

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer': customer
    }
    return render(request, 'plp_ecommerce/customer_detail.html', context)
