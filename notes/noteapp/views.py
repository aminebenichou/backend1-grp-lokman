from django.shortcuts import redirect, render
from .models import Note

# Create your views here.
def Home(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, "index.html", context)


def createNote(request):
    note = Note.objects.all()
    title = request.POST['Title']
    content = request.POST['Content']
    
    note.create(
        title=title,
        content=content
    )

    return redirect(Home)