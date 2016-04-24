from django.shortcuts import render

# Create your views here.
def profil(request):
    return render(request,'profil.html')

def cheval(request):
    return render(request,'cheval.html')

def encadrement(request):
    return render(request,'encadrement.html')

def homepage(request):
    return render(request,'homepage.html')
