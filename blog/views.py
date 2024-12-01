from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import *
from django.urls import reverse_lazy


def index(request):
    return render(request, 'blog/index.html')

def history(request):
    return render(request, 'blog/history.html')

def about(request):
    return render(request, 'blog/about.html')

class GroupsListView(ListView):
    model = Groups
    template_name = 'blog/groups.html'
    context_object_name = 'groups'


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
