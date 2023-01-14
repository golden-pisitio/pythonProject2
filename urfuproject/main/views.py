from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def map(request):
    return render(request, 'main/map.html')


def skills(request):
    return render(request, 'main/skills.html')


def job(request):
    return render(request, 'main/job.html')







