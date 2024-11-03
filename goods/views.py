from django.shortcuts import render, get_list_or_404 # get_object_or_404
from goods.models import Products
from django.core.paginator import Paginator

def catalog(request,category_slug):
	page=request.GET.get('page', 1)
	if category_slug=='vse-tovary':
		goods=Products.objects.all()
	else:
		goods=get_list_or_404(Products.objects.filter(category__slug=category_slug))

	paginator = Paginator(goods, 3)
	current_page = paginator.page(int(page))

	context={
		'goods':current_page,
		'slug_url':category_slug,
	}
	return render(request, 'goods/catalog.html', context=context)

def products(request, product_slug):
	prod=Products.objects.get(slug=product_slug)
	context={
		'prod':prod,
	}
	return render(request, 'goods/products.html', context=context)
