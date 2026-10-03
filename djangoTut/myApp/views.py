from django.shortcuts import render, HttpResponse

# Create your views here.
def test_page(request):
    # return HttpResponse("Hello World, You are at Home")
    return render(request, 'test_page.html')

def child_page(request):
    return HttpResponse("Hello from child route")