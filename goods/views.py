from django.shortcuts import render, get_list_or_404 # get_object_or_404
from goods.models import Products
from django.core.paginator import Paginator

def catalog(request,category_slug):

	page=request.GET.get('page', 1)
	on_sale=request.GET.get('on_sale', None)
	order_by=request.GET.get('order_by', None)

	if category_slug=='vse-tovary':
		goods=Products.objects.all()
	else:
		goods=get_list_or_404(Products.objects.filter(category__slug=category_slug))

	if on_sale:
		goods=goods.filter(discount__gt=0)

	if order_by and order_by != 'default':
		goods=goods.order_by(order_by)

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
