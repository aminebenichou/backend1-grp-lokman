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


def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect(Home)


def edit_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['notecontent']
        note.save()
        return redirect(Home)
    else:
        return render(request, 'edit.html', {'note': note})