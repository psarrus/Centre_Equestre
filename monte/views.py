from django.shortcuts import render


def encadrement(request):
    return render(request,'encadrement.html')


def homepage(request):
    return render(request,'homepage.html')
