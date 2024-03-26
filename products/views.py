from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product 
from .forms import ProductForm , CommentForm
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProduct ,paginationProducts


# def products(request):
# return HttpResponse("bib nasho")

# def product(request, pk):
# return HttpResponse("bib nasho"+ str(pk))
pr = [
    {
        'id': '1',
        'title': 'hamid',
        'description': 'ksjdsjsids'
    },
    {

        'id': '2',
        'title': 'sima',
        'description': 'ksjsssssssids'
    }
]


def products(request):
    product1 , search_query =searchProduct(request)
    custom_range ,product1 ,paginator =paginationProducts(request,product1,6)

    context = {'products': product1 ,'serach_query':search_query ,'paginator':paginator , 'custom_range':custom_range}
    return render(request, 'products/products.html', context)


def product(request, pk):
    # productObj=None
    # for i in pro:
    #     if i['id'] == pk:
    #         productObj=i
    # return render(request, 'products/single-product.html', {'product':productObj})
    #

    productObj = Product.objects.get(id=pk)
    form=CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.product=productObj
        comment.owner= request.user.profile
        comment.save()


        productObj.getVoteCount
        messages.success(request, 'your comment was successfully submitted')
        return redirect('product',pk=productObj.id)


    tags = productObj.tags.all()
    return render(request, 'products/single-product.html', {'productObj': productObj, 'tags': tags , 'form':form})

@login_required(login_url='login')
def createProduct(request):
    profile=request.user.profile
    form = ProductForm()
    if request.method == 'POST':
        # print(request.POST['title'])
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.owner=profile
            product.save()
            return redirect('account')

    context = {'form': form}
    return render(request, "products/product_form.html", context)

@login_required(login_url='login')
def updateProduct(request, pk):
    profile=request.user.profile
    productObj = profile.product_set.get(id=pk) 
    form = ProductForm(instance=productObj)
    if request.method == 'POST':
        # print(request.POST['title'])
        form = ProductForm(request.POST, request.FILES, instance=productObj)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, "products/product_form.html", context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    profile=request.user.profile
    product =profile.product_set.get(id=pk) 
    if request.method == "POST":
        product.delete()
        return redirect('products')
    context = {'object': product}
    return render(request, 'delete_template.html', context)
