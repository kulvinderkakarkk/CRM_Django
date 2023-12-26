from django.shortcuts import render

# Create your views here.
def allcustomers(request):
    return render(request, 'list.html', {})