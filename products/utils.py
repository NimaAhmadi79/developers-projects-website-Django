from .models import Product, Tag
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage


def paginationProducts(request, products, results):
    page = request.GET.get('page')
    paginator=Paginator(products,results)
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        page=1
        products=paginator.page(page) 
    except EmptyPage:
        page=paginator.num_pages 
        products=paginator.page(page)   


    leftIndex=(int(page)-2)

    if leftIndex <1:
        leftIndex=1 

    rightIndex=(int(page)+3)

    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages

    custom_range=range(leftIndex,rightIndex)
    



    return custom_range , products ,paginator





def searchProduct(request):

    search_query= ''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    tags=Tag.objects.filter(name__iexact=search_query)
    product1 = Product.objects.distinct().filter(
      Q(title__icontains=search_query) |
      Q(description__icontains=search_query)|
      Q(owner__name__icontains=search_query)|
      Q(tags__in=tags)  
    )

    return  product1 , search_query