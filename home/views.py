from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def account(request):
    return render(request, 'account.html')


def search(request):
    return render(request, 'search.html')
