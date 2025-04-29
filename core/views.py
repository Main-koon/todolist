from django.shortcuts import render
from .models import Note

def index(request):
    notes = Note.objects.all()
    return render(request, "core/index.html", {'notes': notes})


def  about(request):
    return render(request, "core/about.html")

def editing_note(request):
    return render(request, "core/editing_note.html")

