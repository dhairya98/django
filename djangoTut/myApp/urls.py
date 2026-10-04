from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_page, name='test_page'),
    path('child1/', views.child_page, name='child_page'),
    
    path('child2/', views.all_data, name='all_data'),
    path('child2/<int:id>/', views.single_data, name='single_data'), 

    path('stores/', views.store_view, name='store_view')
]
