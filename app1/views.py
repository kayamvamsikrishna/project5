from django.shortcuts import render

# Create your views here.
def gh(request):
    d={'name':'kishore','age':24}
    return render(request,'h.html',d)