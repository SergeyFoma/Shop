from django.shortcuts import render
from goods.models import Products

def catalog(request,category_slug):
	if category_slug=='vse-tovary':
		goods=Products.objects.all()
	else:
		goods=Products.objects.filter(category__slug=category_slug)
	context={
		'goods':goods,
	}
	return render(request, 'goods/catalog.html', context=context)

def products(request, product_slug):
	prod=Products.objects.get(slug=product_slug)
	context={
		'prod':prod,
	}
	return render(request, 'goods/products.html', context=context)
