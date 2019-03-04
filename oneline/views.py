from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, "oneline/index.html")



def cafemenu(request):
    
    return render(request, "oneline/cafemenu.html")