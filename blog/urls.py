from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('about/', views.about, name='about'),
    path('faculties/', views.faculties, name='faculties'),
    path('admissions/', views.admissions, name='admissions'),
    path('contact/', views.contact, name='contact'),
]
