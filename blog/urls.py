from django.urls import path
from . import views
from blog.views import *
from django.conf.urls import handler404
from django.shortcuts import render


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)


# Настройка для обработки 404 ошибок
handler404 = 'blog.urls.custom_page_not_found'


urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('about/', views.about, name='about'),
    path('groups/', list_schedules, name='groups'),
    path('groups/open/<int:file_id>/', views.open_schedule_file, name='open_schedule_file'),
    path('groups/add/', AddGroupView.as_view(), name='add_group'),
    path('groups/add-lesson/', AddLessonView.as_view(), name='add_lesson'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),  # Детальная страница группы
    path('admissions/', views.admissions, name='admissions'),
    path('contact/', views.contact, name='contact'),
    path('schedule-file/', schedule_file_view, name='schedule_file'),
    # path('open-schedule/', open_schedule_file, name='open_schedule'),

]
