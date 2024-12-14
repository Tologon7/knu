from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import *
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import FileResponse, HttpResponse
import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import ScheduleFile
from .forms import ScheduleFileForm

def index(request):
    return render(request, 'blog/index.html')

def history(request):
    return render(request, 'blog/history.html')

def about(request):
    return render(request, 'blog/about.html')


def open_schedule_file(request, file_id):
    # Получаем файл по ID
    schedule_file = get_object_or_404(ScheduleFile, id=file_id)

    # Проверяем, существует ли файл для поля c1b11
    if schedule_file.c1b11:
        return redirect(schedule_file.c1b11.url)
    else:
        # В случае отсутствия файла перенаправляем на другую страницу
        return redirect('error_page')


def list_schedules(request):
    # Получаем последнюю запись
    schedule_file = ScheduleFile.objects.last()

    # Собираем данные для последнего объекта, чтобы передать их в шаблон
    file_data = []
    if schedule_file:
        file_data.append({
            'id': schedule_file.id,
            'c2b11': schedule_file.c2b11.url if schedule_file.c2b11 else None,
            'c1b11': schedule_file.c1b11.url if schedule_file.c1b11 else None,
            'c3b9': schedule_file.c3b9.url if schedule_file.c3b9 else None,
            'c2b9': schedule_file.c2b9.url if schedule_file.c2b9 else None,
            'c1b9': schedule_file.c1b9.url if schedule_file.c1b9 else None,
            'it9': schedule_file.it9.url if schedule_file.it9 else None,
        })

    return render(request, 'blog/groups.html', {'file_data': file_data})


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
            # Если файл существует, удаляем старый файл в соответствующем поле
            if schedule_file:
                # Пример для удаления файла в поле c1b11
                if schedule_file.c1b11:
                    schedule_file.c1b11.delete()
                # Аналогично для других полей:
                if schedule_file.c2b11:
                    schedule_file.c2b11.delete()
                if schedule_file.c3b9:
                    schedule_file.c3b9.delete()
                # Добавьте проверки для других полей, если нужно

            # Сохраняем новый файл
            form.save()
            return redirect('schedule_file')  # Перенаправляем на ту же страницу после успешной загрузки
    else:
        form = ScheduleFileForm()

    # Рендерим шаблон
    return render(request, 'blog/schedule_file.html', {
        'form': form,
        'schedule_file': schedule_file,
    })
