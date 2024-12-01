from django.urls import path
from . import views
from blog.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('about/', views.about, name='about'),
    path('groups/', GroupsListView.as_view(), name='groups'),
    path('groups/add/', AddGroupView.as_view(), name='add_group'),
    path('groups/add-lesson/', AddLessonView.as_view(), name='add_lesson'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),  # Детальная страница группы
    path('admissions/', views.admissions, name='admissions'),
    path('contact/', views.contact, name='contact'),
]
