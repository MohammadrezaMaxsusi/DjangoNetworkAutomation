from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def commandArea(request):
    return render(request , 'commandArea.html')

