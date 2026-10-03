from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import FirstModel

def test_page(request):
    return render(request, 'test_page.html')

def child_page(request):
    return HttpResponse("Hello from child route")

def all_data(request):
    data = FirstModel.objects.all()
    return render(request, 'all_data.html', {'data': data})

def single_data(request, id):
    # Using get_object_or_404 is cleaner to avoid runtime server crashes if an ID doesn't exist
    item = get_object_or_404(FirstModel, id=id)
    return render(request, 'single_data.html', {'item': item})
