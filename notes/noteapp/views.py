from django.shortcuts import redirect, render
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Home(request):
        # authenticate(username="admin2", password="admin")
        # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        notes = Note.objects.filter(user__id=request.user.id)
        context = {
            'notes': notes
        }
        return render(request, "index.html", context)
    else:
        return redirect(SignInView)

def SignUpView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects
        user.create_user(username=username, password=password)
        return redirect(Home)
    if request.method == 'GET':
        return render(request, "signup.html")

def SignOutView(request):
    logout(request)
    return redirect(Home)

def SignInView(request):
    if request.user.is_authenticated:
        print("hello")
        return redirect(Home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        if user is None:
            return render(request, "signin.html", {"error": "Invalid username or password"})
        else:
            return redirect(Home)
    if request.method == 'GET':
        return render(request, "signin.html")


def createNote(request):
    note = Note.objects.all()
    title = request.POST['Title']
    content = request.POST['Content']
    
    note.create(
        title=title,
        content=content,
        user=request.user
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