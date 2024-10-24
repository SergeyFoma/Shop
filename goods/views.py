from django.shortcuts import render

def catalog(request):
	context={

	}
	return render(request, 'goods/catalog.html', context)

def products(request):
	context={

	}
	return render(request, 'goods/products.html', context)
