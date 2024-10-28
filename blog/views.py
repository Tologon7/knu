from django.shortcuts import render

def base(request):
    return render(request, 'blog/base.html')

def index(request):
    return render(request, 'blog/index.html')

def history(request):
    return render(request, 'blog/history.html')

def about(request):
    return render(request, 'blog/about.html')

def faculties(request):
    return render(request, 'blog/faculties.html')

def admissions(request):
    return render(request, 'blog/admissions.html')

def contact(request):
    return render(request, 'blog/contact.html')
