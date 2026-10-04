from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import FirstModel, Store
from .forms import FirstModelForm

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

def store_view(request):
    stores = None
    if request.method == 'POST':
        form = FirstModelForm(request.POST)
        if(form.is_valid()):
            final_data=form.cleaned_data['dataOnForm']
            stores=Store.objects.filter(first_models=final_data)
    else:
        form = FirstModelForm()

    return render(request, 'stores.html', {'stores': stores, 'form': form})

# def store_view(request):
#     form = FirstModelForm(request.GET or None)
#     stores = Store.objects.all()
    
#     if request.method == 'POST':
#         form = FirstModelForm(request.POST)
#         if form.is_valid():
#             selected_item = form.cleaned_data['dataOnForm']
            
#             stores = Store.objects.filter(first_models=selected_item)
            
#     else:
#         form = FirstModelForm()

#     return render(request, 'stores.html', {'stores': stores, 'form': form})