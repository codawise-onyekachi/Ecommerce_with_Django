from django.shortcuts import render
from .models import Product
#from django.http import HttpResponse
#from django.shortcuts import HttpResponse

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'plp_ecommerce/product_list.html', context)
