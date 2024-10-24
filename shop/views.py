from django.shortcuts import render

def index(request):
	a='INDEX'
	context={
		'a':a,
	}
	return render(request, 'shop/index.html', context)
