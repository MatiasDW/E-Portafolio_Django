from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def index(request):

    name = 'John'

    return render(request, 'index.html', {'nombre': name},)

def counter(request):
    #text=request.POST['text']
    return render(request, 'counter.html')