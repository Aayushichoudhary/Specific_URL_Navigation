from django.shortcuts import render

# Create your views here.

def p1(request):
    return render(request,'person1.html')
    