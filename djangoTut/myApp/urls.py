from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_page, name='Test Page'),
    # nested routes below
    path('child1/', views.child_page, name='Child Page'),
]