from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page')
    try:
        page_obj= paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:  
        page_obj = paginator.page(paginator.num_pages)
        
    return render(request, 'Product/product_list.html',{'product_list':page_obj,})


def product_detail(request, slug):
    product_detail = Product.objects.get(PRDSlug=slug)

    return render(request, 'Product/product_detail.html', {'product_detail':product_detail})