from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, "oneline/index.html")



def cafemenu(request):
    
    return render(request, "oneline/cafemenu.html")


def aboutpetercat(request):
    
    return render(request, "oneline/aboutpetercat.html")

def booksalon(request):
    
    return render(request, "oneline/booksalon.html")