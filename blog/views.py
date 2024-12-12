from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import *
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import FileResponse, HttpResponse
import os
from django.shortcuts import render, redirect
from .models import ScheduleFile
from .forms import ScheduleFileForm

def index(request):
    return render(request, 'blog/index.html')

def history(request):
    return render(request, 'blog/history.html')

def about(request):
    return render(request, 'blog/about.html')


def open_schedule_file(request):
    # Попробуем получить последний загруженный файл из модели ScheduleFile
    schedule_file = ScheduleFile.objects.latest('updated_at')

    if schedule_file:
        # Если файл существует, направляем на URL файла
        return redirect(schedule_file.file.url)
    else:
        return HttpResponse("Файл не найден", status=404)


# class GroupsListView(View):
#     model = Groups
#     # template_name = 'blog/group.html'
#     context_object_name = 'group'
#
#     def get_queryset(self):
#         return Groups.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # Получаем последний загруженный файл расписания
#         try:
#             schedule_file = ScheduleFile.objects.latest('updated_at')
#         except ScheduleFile.DoesNotExist:
#             schedule_file = None
#
#         context['schedule_file'] = schedule_file  # Передаем файл в контекст
#
#         return context


class GroupDetailView(DetailView):
    model = Groups
    template_name = 'blog/group_detail.html'
    context_object_name = 'group'

    def get_queryset(self):
        return Groups.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weeks'] = self.object.weeks.prefetch_related('lessons').all()
        return context


class AddGroupView(CreateView):
    model = Groups
    template_name = 'blog/add_group.html'
    fields = '__all__'

    success_url = reverse_lazy('groups')

class AddLessonView(CreateView):
    models = Lesson
    template_name = 'blog/add_lesson.html'
    fields = '__all__'

    success_url = reverse_lazy('groups')

    def get_queryset(self):
        return Lesson.objects.all()

def admissions(request):
    return render(request, 'blog/admissions.html')

def contact(request):
    return render(request, 'blog/contact.html')

def schedule_file_view(request):
    try:
        # Получаем самый последний файл
        schedule_file = ScheduleFile.objects.latest('updated_at')
    except ScheduleFile.DoesNotExist:
        schedule_file = None

    if request.method == 'POST':
        form = ScheduleFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Если файл существует, удаляем старый
            if schedule_file:
                schedule_file.file.delete()
            form.save()
            return redirect('schedule_file')  # Перенаправляем на ту же страницу после успешной загрузки
    else:
        form = ScheduleFileForm()

    # Рендерим шаблон
    return render(request, 'blog/schedule_file.html', {
        'form': form,
        'schedule_file': schedule_file,
    })
