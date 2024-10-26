from django.shortcuts import render
from goods.models import Categories

def index(request):
	categories=Categories.objects.all()
	context={
		'categories':categories,
	}
	return render(request, 'shop/index.html', context)

def about(request):
	context={

	}
	return render(request, 'shop/about.html', context)
