from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'finalproject/index.html')


def about(request):
    return render(request, 'finalproject/about.html')


def blog(request):
    return render(request, 'finalproject/blog.html')


def portfolio(request):
    return render(request, 'finalproject/portfolio.html')


def contact(request):
    return render(request, 'finalproject/contact.html')