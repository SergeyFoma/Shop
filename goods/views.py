from django.shortcuts import render
from goods.models import Products

def catalog(request):
	goods=Products.objects.all()
	context={
		'goods':goods,
	}
	return render(request, 'goods/catalog.html', context)

def products(request):
	context={

	}
	return render(request, 'goods/products.html', context)
