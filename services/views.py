from django.shortcuts import render

def servindex(request):
    return render(request, 'services/usl.html')