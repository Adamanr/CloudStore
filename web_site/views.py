from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def store(request):
    return render(request, 'store.html')


def registration(request):
    return render(request, 'registration.html')


def authorization(request):
    return render(request, 'authorization.html')