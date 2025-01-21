from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def  about(request):
    return render(request, "core/about.html")

def editing_note(request):
    return render(request, "core/editing_note.html")